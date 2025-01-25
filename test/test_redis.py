import redis

r = redis.StrictRedis(host='192.168.100.101', port=6379, db=0)

r.set("KEY", "VALUE")
print(r.get("KEY"))
 