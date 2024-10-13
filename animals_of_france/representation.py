from pathlib import PurePath

from pydantic import BaseModel

from animals_of_france.models import Resource
from animals_of_france.translation import translate


class Image(BaseModel):
    url: str
    foto_date: str
    coords: str


class Animal(BaseModel):
    id: str
    images: list[Image]

    latin: str
    fr: str
    en: str
    ru: str

    @property
    def title(self) -> str:
        return f"{self.fr} / {self.en} / {self.ru}"

    @staticmethod
    def from_model(resources: list[Resource]) -> "Animal":
        first_resource = resources[0]

        latin_name = Animal._get_latin_name(first_resource.asset_folder)
        fr, en, ru = translate(latin_name)

        return Animal(
            id=latin_name.lower().replace(" ", "_"),
            images=[
                Image(
                    url=resource.secure_url,
                    foto_date=resource.metadata.foto_date,
                    coords=resource.metadata.coords,
                )
                for resource in resources
            ],
            latin=latin_name,
            fr=fr,
            en=en,
            ru=ru,
        )

    @staticmethod
    def _get_latin_name(folder_name: str) -> str:
        return PurePath(folder_name).name
