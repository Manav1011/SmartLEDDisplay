from django.urls import re_path
from .consumers import SerialConsumer

websocket_urlpatterns = [
    re_path(r"serial_communication/(?P<id>.+)$", SerialConsumer.as_asgi()),
]