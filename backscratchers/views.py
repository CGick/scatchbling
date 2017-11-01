# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from backscratchers.models import BackScratcher
from backscratchers.serializers import BackScratcherSerializer


@csrf_exempt
def backscratcher_list(request):
    """
    List all backscratchers, or create a new backscratcher.
    """
    if request.method == "GET":
        backscratchers = BackScratcher.objects.all()
        serializer = BackScratcherSerializer(backscratchers, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == "POST":
        data = JSONParser().parse(request)
        serializer = BackScratcherSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def backscratcher_detail(request, pk):
    """
    Retrieve, update, or delete a backscratcher.
    """
    try:
        backscatcher = BackScratcher.objects.get(pk=pk)
    except BackScratcher.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == "GET":
        serializer = BackScratcherSerializer(backscatcher)
        return JsonResponse(serializer.data)

    elif request.method == "PUT":
        data = JSONParser().parse(request)
        serializer = BackScratcherSerializer(backscatcher, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == "DELETE":
        backscatcher.delete()
        return HttpResponse(status=204)
