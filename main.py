import flet as ft
from incolume.py.flet_routing_tutorial.views.routes import router
from incolume.py.flet_routing_tutorial.user_controls.app_bar import NavBar


def main(page: ft.Page):
    page.theme_mode = "dark"
    page.appbar = NavBar(page)
    page.on_route_change = router.route_change
    router.page = page
    page.add(router.body)
    page.go("/")


if __name__ == "__main__":  # pragma: no cover
    ft.app(target=main, assets_dir="assets")
