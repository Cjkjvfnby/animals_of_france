import json
import os
from logging import warning

from dotenv import load_dotenv
from pydantic.json import pydantic_encoder

from animals_of_france.configuration import IMAGE_DUMP_PATH
from animals_of_france.models import Resource, ResourceResponse

# Setup before cloudinary import.
load_dotenv()

import cloudinary  # noqa: E402
import cloudinary.api  # noqa: E402
import cloudinary.uploader  # noqa: E402


def _get_images() -> list[Resource]:
    return ResourceResponse(
        **cloudinary.api.resources(
            resource_type="image",
            type="upload",
            asset_folder="animals_of_france",
            format="jpg",
        )
    ).resources


def _save_to_disc(resource: list[Resource]) -> None:
    with IMAGE_DUMP_PATH.open("w") as f:
        json.dump(resource, f, default=pydantic_encoder, indent=4)
    warning(f"saved to {IMAGE_DUMP_PATH}")


def download_assets() -> None:
    print(os.environ)  # noqa: T201

    if "CLOUDINARY_URL" not in os.environ:
        message = "CLOUDINARY_URL is not provided"
        raise Exception(message)  # noqa: TRY002

    images = _get_images()
    _save_to_disc(images)


if __name__ == "__main__":
    download_assets()
