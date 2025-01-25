
# Version 2
# chat/consumers.py
from cgitb import text
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


class KitchenConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        ids = self.scope['url_route']['kwargs']['ids']

        self.watch_list = json.loads(ids)
        self.group_name = '__KitchenConsumer__'
        # saas 2020/09/27
        self.group_name = saas.group_name(self.scope, self.group_name)
        print(self.group_name, ids)

        # Join room group
        await self.channel_layer.group_add(
            self.group_name,
            self.channel_name
        )
        log.info("[########## create KitchenConsumer {0} ##############]".format(self.group_name))
        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(
            self.group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        log.info("############## receive {0} {1} {2}".format(self.group_name, self.channel_name, text_data))
        if len(text_data)>4 and text_data[0:4]=="ping":
            await self.send(text_data="pong")

    # 注文追加の通知
    async def order_add(self, event):

        master_id = int(event['master_id'])
        log.info("############### kitchen_data")

        if master_id in self.watch_list:
            result = json.dumps({
                "kitchen_data": event['kitchen_data'],
                "type": "order_add"
            }, default=support_datetime_default)
            await self.send(text_data=result)

    async def order_delete(self, event):

        detail_id = event['detail_id']
        log.info("############### order_delete : {0}".format(detail_id))

        result = json.dumps({
            "detail_id": detail_id,
            "type": "order_delete"
        }, default=support_datetime_default)
        # if master_id in self.watch_list:
        await self.send(text_data=result)

        
    async def order_change(self, event):

        log.info("############### order_change")

        result = json.dumps({
            "detail_id": "",
            "type": "order_change"
        }, default=support_datetime_default)
        # if master_id in self.watch_list:
        await self.send(text_data=result)
