"""index view module."""

import logging

import flet as ft
from incolume.py.flet_routing_tutorial.views.Router import (
    DataStrategyEnum,
    Router,
)
from incolume.py.flet_routing_tutorial.State import State


def index_view(router_data: Router = None) -> ft.Control:
    """index_view function.

    :param router_data:
    :return:
    """

    def send_data(e: ft.ControlEvent) -> ft.Control | None:
        """Send data function.

        :param e:
        :return:
        """
        if text_field.value == '':
            return None

        if router_data:
            match router_data.data_strategy:
                case DataStrategyEnum.QUERY:
                    e.page.go('/data', data=text_field.value)
                case DataStrategyEnum.ROUTER_DATA:
                    router_data.set_data('data', text_field.value)
                    e.page.go('/data', data=text_field.value)
                case DataStrategyEnum.CLIENT_STORAGE:
                    e.page.client_storage.set('data', text_field.value)
                    e.page.go('/data')
                case DataStrategyEnum.STATE:
                    state = State('data', text_field.value)
                    logging.debug(state)
                    e.page.go('/data')
        else:
            e.page.go('/data')

    text_field = ft.TextField()
    send_button = ft.ElevatedButton('Send')
    send_button.on_click = send_data
    return ft.Column(
        [
            ft.Row(
                [
                    ft.Text('Welcome to my Flet Router Tutorial', size=50),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
            ),
            ft.Row(
                [text_field, send_button],
                alignment=ft.MainAxisAlignment.CENTER,
            ),
        ],
    )
