from django.shortcuts import render
from .Serializers import ParamsSerializer
from rest_framework.response import Response
from rest_framework import status
from .models import Params
from rest_framework import generics

class ParamsAPIView(generics.CreateAPIView):
    queryset = Params.objects.all()
    serializer_class = ParamsSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        # Perform regression on the posted parameters
        params = serializer.save()
        a = params.Age
        b = params.Asset
        c = params.Financial
        result = Regression(a, b, c)

        headers = self.get_success_headers(serializer.data)
        response_data = serializer.data
        response_data['result'] = result  # Include the regression result in the response
        return Response(response_data, status=status.HTTP_201_CREATED, headers=headers)


def Regression(a, b, c):
    C = 0.01 * c + 0.23 * b + 0.012 * a 
    return C
