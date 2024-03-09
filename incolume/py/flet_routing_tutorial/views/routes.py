from incolume.py.flet_routing_tutorial.views.Router import Router, DataStrategyEnum
from incolume.py.flet_routing_tutorial.views.index_view import IndexView
from incolume.py.flet_routing_tutorial.views.profile_view import ProfileView
from incolume.py.flet_routing_tutorial.views.settings_view import SettingsView
from incolume.py.flet_routing_tutorial.views.data_view import DataView

router = Router(DataStrategyEnum.QUERY)

router.routes = {
    "/": IndexView,
    "/profile": ProfileView,
    "/settings": SettingsView,
    "/data": DataView,
}
