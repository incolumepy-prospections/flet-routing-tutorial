"""Principal Module."""

from pathlib import Path

import toml

__author__ = '@britodfbr'  # pragma: no cover


confproject = Path(__file__).parents[3] / 'pyproject.toml'
__version__ = toml.load(confproject)['tool']['poetry']['version']
