# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from backscratchers.models import BackScratcher
from backscratchers.serializers import BackScratcherSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class BackscratcherList(APIView):
    """
    List all backscratchers, or create a new backscratcher.
    """
    def get(self, request, format=None):
        backscratchers = BackScratcher.objects.all()
        serializer = BackScratcherSerializer(backscratchers, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
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


class BackscratcherDetail(APIView):
    """
    Retrieve, update, or delete a backscratcher.
    """
    def get_object(self, pk):
        try:
            return BackScratcher.objects.get(pk=pk)
        except BackScratcher.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        backscratcher = self.get_object(pk)
        serializer = BackScratcherSerializer(backscratcher)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        backscratcher = self.get_object(pk)
        serializer = BackScratcherSerializer(
            backscratcher,
            data=request.data
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    def delete(self, request, pk, format=None):
        backscratcher = self.get_object(pk)
        backscratcher.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
