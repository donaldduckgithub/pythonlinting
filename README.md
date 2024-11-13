# My first game

A preview of the game:

[<img alt = "My first game" src = "https://i.imgur.com/rZpWJV9.png" width = 25% />](https://i.imgur.com/rZpWJV9.png)

This is my first game:

- Its main purpose is to show how we configure Poetry and the `pyproject.toml` file for better dependency management, and adds a formatter and a linter as well as a CI setup to check all this.
- But of course the game is playable. You can walk around in a 3D world :).

## Installing dependencies

Using [Poetry](https://python-poetry.org/):

```console
poetry install
```

This will also build the Cython extensions.
If you ever need to rebuild them, you can do:

```console
poetry build
```

## Running

Using Poetry:

```console
poetry run python main.py
```