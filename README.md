[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/format.json)](https://github.com/astral-sh/ruff_format)


Catalog of animals I have seen in France.

The result is deployed as [GitHub pages](https://cjkjvfnby.github.io/animals_of_france/index.html)


# Development

## Install dev requirements
```shell
pip install -r requirements-dev.txt
```

## Install pre-commit
- add hooks
  ```shell
  pre-commit install
  pre-commit install --hook-type commit-msg
  ```
- update to the latest versions
  ```shell
  pre-commit autoupdate
  ```

## Formatting and Linting
```shell
pre-commit run --all-files
```

## Run test
```shell
pytest --cov=animals_of_france --cov-report html
```
