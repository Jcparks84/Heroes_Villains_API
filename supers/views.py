from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import supersSerializer
from .models import Supers
from rest_framework import status
from django.shortcuts import get_object_or_404


@api_view(['GET', 'POST'])
def supers_list(request):
    if request.method == 'GET':
        supers = Supers.objects.all()
        serializer = supersSerializer(supers, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = supersSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'PUT', 'DELETE'])
def supers_detail(request, pk):
    product = get_object_or_404(Super, pk=pk)
    if request.method == 'GET':
        serializer = supersSerializer(super)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = supersSerializer(super, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    elif request.method == 'DELETE':
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    # super_type_param = request.query_params.get('supertype')
    # sort_param = request.query_params.get('sort')

    # supers = Supers.objects.all()

    # if super_type_param:
    #     supers = supers.filter(super_type_param=super_type_param)

    # if sort_param:
    #     supers = supers.order_by(sort_param)


    # serializer = supersSerializer(supers, many=True)

    # return Response(serializer.data)
