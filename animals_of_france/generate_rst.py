from itertools import groupby, zip_longest
from logging import warning

from jinja2 import Environment, PackageLoader, select_autoescape
from pydantic import TypeAdapter

from animals_of_france.configuration import (
    DASHBOARD,
    GENERATED_FOLDER,
    IMAGE_DUMP_PATH,
    TOC_TREE_FILE,
)
from animals_of_france.models import Resource
from animals_of_france.representation import Animal

env = Environment(
    loader=PackageLoader("animals_of_france"), autoescape=select_autoescape()
)


def _make_file(file_name: str, species: Animal) -> None:
    template = env.get_template("animal.tmpl.rst")

    text = template.render(animal=species)

    GENERATED_FOLDER.mkdir(exist_ok=True)
    with (GENERATED_FOLDER / file_name).open("w", encoding="utf8") as f:
        f.write(text)


def _empty_lines_needed(total: int, number_of_columns: int) -> int:
    extra = total % number_of_columns
    if extra:
        return number_of_columns - extra
    return 0


def _generate_dash_board(animals: list[Animal]) -> None:
    template = env.get_template("base.tmpl.rst")
    rows = list(zip_longest(*[iter(animals)] * 3))

    with DASHBOARD.open("w", encoding="utf8") as f:
        f.write(template.render(rows=rows))


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
    template = env.get_template("generated.tmpl.rst")

    text = template.render(names=[x[:-4] for x in base_item_list])

    with TOC_TREE_FILE.open("w", encoding="utf8") as f:
        f.write(text)


if __name__ == "__main__":
    generate_rst()
