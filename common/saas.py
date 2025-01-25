

# return saas id
def group_name(scope, gname):
    headers = scope["headers"]
    request_host = ""
    for k, v in headers:
        if k.decode()=="host":
            request_host = v.decode()
    if request_host!="":
        id = request_host.split('.')
        if id[0]=="192":
            id[0] = "foodlife01"
        return "{0}.{1}".format(id[0], gname)
    return gname
