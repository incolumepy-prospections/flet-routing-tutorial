"""App_bar module."""

import flet as ft


def nav_bar(page: ft.Page) -> ft.AppBar:
    """Navbar.

    :param page:
    :return:
    """
    return ft.AppBar(
        leading=ft.Icon(ft.icons.TAG_FACES_ROUNDED),
        leading_width=40,
        title=ft.Text('Flet Router'),
        center_title=False,
        bgcolor=ft.colors.SURFACE_VARIANT,
        actions=[
            ft.IconButton(ft.icons.HOME, on_click=lambda _: page.go('/')),
            ft.IconButton(
                ft.icons.PERSON_ROUNDED,
                on_click=lambda _: page.go('/profile'),
            ),
            ft.IconButton(
                ft.icons.SETTINGS_ROUNDED,
                on_click=lambda _: page.go('/settings'),
            ),
        ],
    )
