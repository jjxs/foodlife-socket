# mysite/routing.py
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
import chat.routing
import counter.routing

# websocket通信的根路由
urlpatterns = []
urlpatterns += chat.routing.websocket_urlpatterns
urlpatterns += counter.routing.websocket_urlpatterns

application = ProtocolTypeRouter({
    'websocket': AuthMiddlewareStack(
        URLRouter(
            urlpatterns
        )
    )
})
