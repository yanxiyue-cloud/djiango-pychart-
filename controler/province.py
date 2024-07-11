from people.charts.province import *
from django.http import HttpResponse
import json
def provincemap(request):
    res = chartmap()
    json_res = json.loads(res)
    json_obj = {"code": 200, "msg": "success", "data": json_res}
    res = HttpResponse(json.dumps(json_obj), content_type="application/json;charset=UTF-8")
    return res