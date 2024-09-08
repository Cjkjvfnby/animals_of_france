from datetime import datetime
from itertools import cycle
from logging import warning

from pydantic import TypeAdapter

from animals_of_france.configuration import (
    DASHBOARD,
    GENERATED_FOLDER,
    IMAGE_DUMP_PATH,
    TOC_TREE_FILE,
)
from animals_of_france.models import Resource, ResourceMetadata
from animals_of_france.translation import translate

_empty = Resource(
    asset_id="",
    secure_url="",
    metadata=ResourceMetadata(
        latin_name="",
    ),
)


def _make_file(file_name: str, image: Resource) -> None:
    fr, en, ru = translate(image.metadata.latin_name)

    result = [
        f"{image.metadata.latin_name}",
        "=" * len(image.metadata.latin_name),
        "",
        f"- Français: {fr}",
        f"- English: {en}",
        f"- Русский: {ru}",
        "",
        f".. image:: {image.secure_url}",
        f"   :target: {image.secure_url}",
    ]

    if image.metadata.foto_date:
        taken_at = datetime.strptime(image.metadata.foto_date, "%Y-%m-%d")  # noqa: DTZ007
        result.append(f"\nWas taken at {taken_at.date()}")

    if image.metadata.coords:
        map_url = (
            f"https://www.google.com/maps/search/?api=1&query={image.metadata.coords}"
        )
        result.append(f"\n`Was taken around this place <{map_url}>`_")

    with (GENERATED_FOLDER / file_name).open("w", encoding="utf8") as f:
        f.write("\n".join(result))


def _generate_dash_board(data: list[Resource]) -> None:
    result = [
        ".. list-table::",
        "   :class: field-list",
        "   :widths: 1 1 1",
        "",
    ]

    number_of_columns = 3
    header_check = cycle([True] + [False] * (number_of_columns - 1))

    for image in data:
        is_header = next(header_check)
        sign = "*" if is_header else " "

        fr, en, ru = translate(image.metadata.latin_name)

        result.extend(
            (
                f"   {sign} - .. figure:: {image.secure_url}",
                f"          :target: {image.secure_url}",
                "",
                f"          :doc:`/generated/{image.asset_id}`",
            )
        )

    result.extend(["     -\n"] * (number_of_columns - (len(data) % number_of_columns)))

    result.append("")

    with DASHBOARD.open("w", encoding="utf8") as f:
        f.write("\n".join(result))


def generate_rst() -> None:
    with IMAGE_DUMP_PATH.open() as f:
        data = TypeAdapter(list[Resource]).validate_json(f.read())

    base_item_list = []

    for image in data:
        file_name = f"{image.asset_id}.rst"
        base_item_list.append("generated/" + file_name)
        _make_file(file_name, image)
        _generate_toc_tree(base_item_list)

    _generate_toc_tree(base_item_list)
    _generate_dash_board(data)
    warning("Rst files are generated")


def _generate_toc_tree(base_item_list: list[str]) -> None:
    with TOC_TREE_FILE.open("w", encoding="utf8") as f:
        f.write(".. include:: generated/base.rst\n")
        f.write(".. toctree::\n")
        f.write("   :maxdepth: 2\n")
        f.write("\n")
        for name in base_item_list:
            f.write(f"   {name[:-4]}\n")


if __name__ == "__main__":
    generate_rst()
