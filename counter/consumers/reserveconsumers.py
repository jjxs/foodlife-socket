
# Version 2
# chat/consumers.py
from asgiref.sync import async_to_sync
from channels.generic.websocket import AsyncWebsocketConsumer
import json
import uuid
import common.logger as log
import common.saas as saas

class ReserveConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.group_name = '__ReserveConsumer__'

        # saas 2020/09/27
        self.group_name = saas.group_name(self.scope, self.group_name)
        
        # Join room group
        await self.channel_layer.group_add(
            self.group_name,
            self.channel_name
        )
        log.info("########## create ReserveConsumer {0} ##############".format(self.group_name))
        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(
            self.group_name,
            self.channel_name
        )
    
    async def receive(self, text_data):
        # Log incoming messages for debugging
        log.info(f"Received message: {text_data}")
        data = json.loads(text_data)
        await self.send(text_data=json.dumps(data))

    async def send_message(self, event):
        log.info("############### Send freemenu_order_confirm to WebSocket")
        print(event['data'])
        await self.send(text_data=json.dumps(event['data']))

