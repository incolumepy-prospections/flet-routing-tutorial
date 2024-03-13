"""Router module."""

import logging
from collections.abc import Callable
from enum import Enum
from typing import Any

import flet as ft


class DataStrategyEnum(Enum):
    """DataStrategyEnum class."""

    QUERY = 0
    ROUTER_DATA = 1
    CLIENT_STORAGE = 2
    STATE = 3


class Router:
    """Router class."""

    def __init__(
        self,
        data_strategy: DataStrategyEnum = DataStrategyEnum.QUERY,
    ):
        """Init class."""
        self.data_strategy = data_strategy
        self.data = {}
        self.routes: dict[str, Callable] = {}
        self.body = ft.Container()

    def set_route(self, stub: str, view: Callable) -> None:
        """Set one route.

        :param stub:
        :param view:
        :return:
        """
        self.routes[stub] = view

    def set_routes(self, route_dictionary: dict[str, Callable]) -> None:
        """Sets multiple routes at once.

         Ex: {"/": index_view }

        :param route_dictionary:
        :return:
        """
        self.routes.update(route_dictionary)

    def route_change(self, route) -> None:
        """Route change.

        :param route:
        :return:
        """
        logging.debug('%s: %s', route, type(route))
        _page = route.route.split('?')[0]
        queries = route.route.split('?')[1:]

        for item in queries:
            key = item.split('=')[0]
            value = item.split('=')[1]
            self.data[key] = value.replace('+', ' ')

        self.body.content = self.routes[_page](self)
        self.body.update()

    def set_data(self, key: str, value: str) -> None:
        """Set data.

        :param key:
        :param value:
        :return:
        """
        self.data[key] = value

    def get_data(self, key: str) -> dict[Any, Any]:
        """Get data.

        :param key:
        :return:
        """
        return self.data.get(key)

    def get_query(self, key: str) -> dict[Any, Any]:
        """Get query.

        :param key:
        :return:
        """
        return self.data.get(key)
