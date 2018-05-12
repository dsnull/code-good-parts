import json
from collections import OrderedDict
from django.http import HttpResponse
from django.shortcuts import render
import urllib
from .models import DeviceToken

def render_json_response(request, data, status=None):
    """response を JSON で返却"""
    json_str = json.dumps(data, ensure_ascii=False, indent=2)
    callback = request.GET.get('callback')
    if not callback:
        callback = request.POST.get('callback')  # POSTでJSONPの場合
    if callback:
        json_str = "%s(%s)" % (callback, json_str)
        response = HttpResponse(json_str, content_type='application/javascript; charset=UTF-8', status=status)
    else:
        response = HttpResponse(json_str, content_type='application/json; charset=UTF-8', status=status)
    return response


def register_device(request):
    results = []
    result_dict = []
    if "device_token" in request.GET:
        device_token = urllib.parse.unquote(request.GET.get("device_token"))
        DeviceToken.objects.create(token=device_token)
        result_dict = OrderedDict([
            ('success','1' ),
            ('message', 'your device is registered.')
        ])
    else:
        result_dict = OrdreredDict([
            ('succress','0'),
            ('message', 'your divice is NOT registered.')
        ])


    results.append(result_dict)

    data = OrderedDict([ ('result', results) ])
    return render_json_response(request, data)

