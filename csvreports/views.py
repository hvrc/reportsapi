from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from _source.reporter import *
import json

@csrf_exempt
def downloadCsv(request):
    if request.method == "POST":
        body = json.loads(request.body)
        df = getReport(getDataframe(body["input"]), body["cols"], body["type"])
        buffer = getBuffer(df)
        response = HttpResponse(buffer)
        response["Content-Disposition"] = "attachment; filename=report.csv"
        return response

    return HttpResponse("Send me a POST request!")
