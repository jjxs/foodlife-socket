
# Version 2
# chat/consumers.py
from asgiref.sync import async_to_sync
from channels.generic.websocket import AsyncWebsocketConsumer
import json
import uuid
import common.logger as log
import common.saas as saas

def support_datetime_default(o):
    if isinstance(o, date):
        return o.isoformat()
    raise TypeError(repr(o) + " is not JSON serializable")


class CounterConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        # ids = self.scope['url_route']['kwargs']['ids']
        self.group_name = '__CounterConsumer__'
        
        # saas 2020/09/27
        self.group_name = saas.group_name(self.scope, self.group_name)
        print(self.group_name)

        # Join room group
        await self.channel_layer.group_add(
            self.group_name,
            self.channel_name
        )
        
        log.info("[########## create CounterConsumer {0} ##############]".format(self.group_name))
        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(
            self.group_name,
            self.channel_name
        )


    # channel_layer = channels.layers.get_channel_layer()
    # channel_layer.group_send(
    #     '__CounterConsumer__',
    #     {
    #         'type': 'send',
    #         'data': { 
    #             'type': 'pay',
    #             'faxprice': 0,
    #             'price': 0,
    #          }
    #     })
    async def sendPrice(self, event):
        log.info("########## sendPrice ##############")
        await self.send(text_data=json.dumps(event['data']))

