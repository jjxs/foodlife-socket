# chat/routing.py
from django.conf.urls import url

from .consumers.orderconsumers import OrderConsumer
from .consumers.seatconsumers import SeatConsumer
from .consumers.kitchenconsumers import KitchenConsumer
from .consumers.counterconsumers import CounterConsumer
from .consumers.staffconsumers import StaffConsumer
from .consumers.reserveconsumers import ReserveConsumer

websocket_urlpatterns = [
    #url(r'^ws/counter/$', consumers.CounterConsumer),
    url(r'^ws/seat/(?P<seat_id>[^/]+)/$', SeatConsumer),
    url(r'^ws/kitchen/(?P<ids>[^/]+)/$', KitchenConsumer),
    url(r'^ws/order/$', OrderConsumer),
    url(r'^ws/counter/$', CounterConsumer),
    url(r'^ws/staff/$', StaffConsumer),
    url(r'^ws/reserve/$', ReserveConsumer),
]
