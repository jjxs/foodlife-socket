# import redis

# r = redis.StrictRedis(host='192.168.100.101', port=6379, db=0)

# r.set("KEY", "VALUE")
# print(r.get("KEY"))


from django.conf import settings

settings.configure(CHANNEL_LAYERS={
    'default': {
        'BACKEND': 'channels_redis.core.RedisChannelLayer',
        'CONFIG': {
            "hosts": [('192.168.100.101', 6379)],
        },
    },
})
# CHANNEL_LAYERS = {
#     'default': {
#         'BACKEND': 'channels_redis.core.RedisChannelLayer',
#         'CONFIG': {
#             "hosts": [('192.168.100.101', 6379)],
#         },
#     },
# }
import channels.layers
from asgiref.sync import async_to_sync
channel_layer = channels.layers.get_channel_layer()

async_to_sync(channel_layer.group_send)(
    '__OrderConfirmConsumer__',
    {
        'type': 'send_message',
        'seat_id': 7,        
        'result': "123123,123"
    })
# async_to_sync(channel_layer.receive)('test_channel')
