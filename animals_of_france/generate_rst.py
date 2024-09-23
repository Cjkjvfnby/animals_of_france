from datetime import datetime
from itertools import cycle, groupby
from logging import warning

from pydantic import TypeAdapter

from animals_of_france.configuration import (
    DASHBOARD,
    GENERATED_FOLDER,
    IMAGE_DUMP_PATH,
    TOC_TREE_FILE,
)
from animals_of_france.models import Resource, ResourceMetadata
from animals_of_france.representation import Animal

_empty = Resource(
    asset_id="",
    secure_url="",
    metadata=ResourceMetadata(
        latin_name="",
    ),
)


def _make_file(file_name: str, species: Animal) -> None:
    result = [
        f"{species.title}",
        "=" * len(species.title),
        "",
        f"- Français: {species.fr}",
        f"- English: {species.en}",
        f"- Русский: {species.ru}",
        "",
    ]

    for image in species.images:
        result.append(f".. image:: {image.url}")
        result.append(f"   :target: {image.url}")

        if image.foto_date:
            taken_at = datetime.strptime(image.foto_date, "%Y-%m-%d")  # noqa: DTZ007
            result.append(f"\nWas taken at {taken_at.date()}")

        if image.coords:
            map_url = f"https://www.google.com/maps/search/?api=1&query={image.coords}"
            result.append(f"\n`Was taken around this place <{map_url}>`__")

        result.append("")

        GENERATED_FOLDER.mkdir(exist_ok=True)
        with (GENERATED_FOLDER / file_name).open("w", encoding="utf8") as f:
            f.write("\n".join(result))


def _empty_lines_needed(total: int, number_of_columns: int) -> int:
    extra = total % number_of_columns
    if extra:
        return number_of_columns - extra
    return 0


def _generate_dash_board(animals: list[Animal]) -> None:
    result = [
        ".. list-table::",
        "   :class: field-list",
        "   :widths: 1 1 1",
        "",
    ]

    number_of_columns = 3
    header_check = cycle([True] + [False] * (number_of_columns - 1))

    for sp in animals:
        is_header = next(header_check)
        sign = "*" if is_header else " "

        result.extend(
            (
                f"   {sign} - .. figure:: {sp.images[0].url}",
                "",
                f"          :doc:`/generated/{sp.id}`",
            )
        )

    empty_lines = _empty_lines_needed(len(animals), number_of_columns)

    result.extend(["     -\n"] * empty_lines)

    result.append("")

    with DASHBOARD.open("w", encoding="utf8") as f:
        f.write("\n".join(result))


def generate_rst() -> None:
    with IMAGE_DUMP_PATH.open() as f:
        resources = TypeAdapter(list[Resource]).validate_json(f.read())

        animals = [
            Animal.from_model(list(group))
            for _, group in groupby(
                sorted(resources, key=lambda x: x.metadata.latin_name),
                lambda x: x.metadata.latin_name,
            )
        ]

    base_item_list = []

    for animal in animals:
        file_name = f"{animal.id}.rst"
        base_item_list.append("generated/" + file_name)
        _make_file(file_name, animal)

    _generate_toc_tree(base_item_list)
    _generate_dash_board(animals)
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
