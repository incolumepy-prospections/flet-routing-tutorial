"""routes module."""

from incolume.py.flet_routing_tutorial.views.data_view import data_view
from incolume.py.flet_routing_tutorial.views.index_view import index_view
from incolume.py.flet_routing_tutorial.views.profile_view import profile_view
from incolume.py.flet_routing_tutorial.views.Router import (
    DataStrategyEnum,
    Router,
)
from incolume.py.flet_routing_tutorial.views.settings_view import settings_view

router = Router(DataStrategyEnum.QUERY)

router.routes = {
    '/': index_view,
    '/profile': profile_view,
    '/settings': settings_view,
    '/data': data_view,
}
