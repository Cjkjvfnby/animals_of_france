from datetime import datetime

from animals_of_france.configuration import IMAGE_DUMP_PATH
from animals_of_france.download_assets import download_assets
from animals_of_france.generate_rst import generate_rst

_ONE_HOUR = 60 * 24


def _need_fetch() -> bool:
    if not IMAGE_DUMP_PATH.exists():
        return True
    modified = datetime.fromtimestamp(IMAGE_DUMP_PATH.stat().st_mtime)
    delta = datetime.now() - modified
    return delta.total_seconds() >= _ONE_HOUR


def _ensure_dump() -> None:
    if _need_fetch():
        download_assets()


def build_docs() -> None:
    _ensure_dump()
    generate_rst()


if __name__ == "__main__":
    build_docs()
