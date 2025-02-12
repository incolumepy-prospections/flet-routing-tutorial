"""Data_view module."""


import flet as ft
from incolume.py.flet_routing_tutorial.views.Router import (
    DataStrategyEnum,
    Router,
)
from incolume.py.flet_routing_tutorial.State import global_state


def data_view(router: Router = None) -> ft.Control:
    """Data view.

    :param router:
    :return:
    """
    text = ft.Text('')

    match router.data_strategy:
        case DataStrategyEnum.QUERY:
            text = ft.Text(f"Query Data: {router.get_query('data')}")
        case DataStrategyEnum.ROUTER_DATA:
            text = ft.Text(f"Router Data: {router.get_query('data')}")
        case DataStrategyEnum.CLIENT_STORAGE:
            text = ft.Text(
                f"Client Storage: {router.page.client_storage.get('data')}",
            )
        case DataStrategyEnum.STATE:
            text = ft.Text(
                f"State: {global_state.get_state_by_key('data').get_state()}",
            )

    return ft.Column(
        [
            ft.Row(
                [
                    ft.Text('Data View', size=50),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
            ),
            ft.Row(
                [
                    text,
                ],
                alignment=ft.MainAxisAlignment.CENTER,
            ),
        ],
    )
