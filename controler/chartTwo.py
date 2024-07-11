from people.charts.chartTwo import *
from django.http import HttpResponse
import json
def chartSecond(request):
    res = charttwo()
    json_res = json.loads(res)
    json_obj = {"code": 200, "msg": "success", "data": json_res}
    res = HttpResponse(json.dumps(json_obj), content_type="application/json;charset=UTF-8")
    return res