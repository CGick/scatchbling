# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from backscratchers.models import BackScratcher
from backscratchers.serializers import BackScratcherSerializer


@api_view(["GET", "POST"])
@csrf_exempt
def backscratcher_list(request, format=None):
    """
    List all backscratchers, or create a new backscratcher.
    """
    if request.method == "GET":
        backscratchers = BackScratcher.objects.all()
        serializer = BackScratcherSerializer(backscratchers, many=True)
        return Response(serializer.data)

    elif request.method == "POST":
        serializer = BackScratcherSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )


@api_view(["GET", "PUT", "DELETE"])
@csrf_exempt
def backscratcher_detail(request, pk, format=None):
    """
    Retrieve, update, or delete a backscratcher.
    """
    try:
        backscatcher = BackScratcher.objects.get(pk=pk)
    except BackScratcher.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = BackScratcherSerializer(backscatcher)
        return Response(serializer.data)

    elif request.method == "PUT":
        serializer = BackScratcherSerializer(
            backscatcher,
            data=request.data
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    elif request.method == "DELETE":
        backscatcher.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
