"""Main module."""

import flet as ft
from incolume.py.flet_routing_tutorial.views.routes import router
from incolume.py.flet_routing_tutorial.user_controls.app_bar import nav_bar
from pathlib import Path


def main(page: ft.Page) -> None:
    """Main function."""
    page.theme_mode = 'dark'
    page.appbar = nav_bar(page)
    page.on_route_change = router.route_change
    router.page = page
    page.add(router.body)
    page.go('/')


if __name__ == '__main__':  # pragma: no cover
    assets = Path(__file__).parent.joinpath('assets')
    ft.app(target=main, assets_dir=assets.as_posix())
