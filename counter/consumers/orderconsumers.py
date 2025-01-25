
# Version 2
# chat/consumers.py
from asgiref.sync import async_to_sync
from channels.generic.websocket import AsyncWebsocketConsumer
import json
import uuid
import common.logger as log
import common.saas as saas


class OrderConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.group_name = '__OrderConsumer__'
        # saas 2020/09/27
        self.group_name = saas.group_name(self.scope, self.group_name)
        print(self.group_name)

        await self.channel_layer.group_add(
            self.group_name,
            self.channel_name
        )
        log.info("[########## create OrderConsumer {0} ##############]".format(self.group_name))
        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(
            self.group_name,
            self.channel_name
        )

    async def send_message(self, event):
        log.info("############### OrderConsumer send_message")
        await self.send(text_data=json.dumps(event['data']))