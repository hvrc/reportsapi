from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from _source.reporter import *

@csrf_exempt
def viewChart(request):
    if request.method == "POST":
        input = request.POST.getlist("input")
        type = request.POST.get("type")
        cols = request.POST.getlist("cols")
        width = request.POST.get("width")
        height = request.POST.get("height")
        df = getDataframe(input[0] if len(input) == 1 else input)
        reportdf = getReport(df, cols, type)
        response = getChartResponse(reportdf, width, height)
        return JsonResponse(response)

    return HttpResponse("Send me a POST request!")
