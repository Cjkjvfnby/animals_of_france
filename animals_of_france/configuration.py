from pathlib import Path

_BASE_DIR = Path(__file__).parent.parent

IMAGE_DUMP_PATH = _BASE_DIR / "data_dump" / "images.json"


GENERATED_FOLDER = _BASE_DIR / "source" / "generated"
TOC_TREE_FILE = _BASE_DIR / "source" / "generated.rst"
DASHBOARD = GENERATED_FOLDER / "base.rst"
