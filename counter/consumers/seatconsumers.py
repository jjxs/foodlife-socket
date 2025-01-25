
# Version 2
# chat/consumers.py
from asgiref.sync import async_to_sync
from channels.generic.websocket import AsyncWebsocketConsumer
import json
import uuid
import common.logger as log
import common.saas as saas


class SeatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.seat_id = self.scope['url_route']['kwargs']['seat_id']
        self.group_name = '__SeatConsumer__' + self.seat_id
        # saas 2020/09/27
        self.group_name = saas.group_name(self.scope, self.group_name)
        print(self.group_name)

        # Join room group
        await self.channel_layer.group_add(
            self.group_name,
            self.channel_name
        )
        log.info("[########## create SeatConsumer {0} {1} ##############]".format(self.group_name, self.channel_name))
        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(
            self.group_name,
            self.channel_name
        )

    # async def receive(self, text_data):
    #     print("############## receive")
    #     print(text_data)
    #     json_data = json.loads(text_data)
    #     print(json_data)
    #     data = json_data['result']
    #     await self.channel_layer.group_send(
    #         self.group_name,
    #         {
    #             'type': 'chat_message',
    #             'result': data
    #         }
    #     )

    # 放題メニュー注文確認完了
    async def freemenu_order_confirm(self, event):

        result = {
            'type': 'freemenu_order_confirm',
            'result': event['result'],
            'freemenu_list': event['freemenu_list']
        }
        log.info("# Send freemenu_order_confirm to WebSocket")
        await self.send(text_data=json.dumps(result))

    # 席利用開始の通知
    async def seat_using_start(self, event):

        log.info("# Send seat_using_start to WebSocket")
        await self.send(text_data=json.dumps({'type': 'seat_using_start'}))

    async def seat_using_stop(self, event):
        log.info("# Send seat_using_stop to WebSocket")
        await self.send(text_data=json.dumps({'type': 'seat_using_stop'}))

    # Receive message from room group
    async def send_message(self, event):
        result = event['result']
        seat_id = event['seat_id']
        if int(self.seat_id) == int(seat_id):

            log.info("# SeatConsumer Send message to WebSocket")
            await self.send(text_data=json.dumps(result))
