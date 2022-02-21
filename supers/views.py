from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import supersSerializer
from .models import Supers
from rest_framework import status
from django.shortcuts import get_object_or_404
from Super_Type.models import SuperType
import supers

@api_view(['GET','POST'])
def supers_list(request):
    type_param = request.query_params.get('super_type')
    supers = Supers.objects.all()

    if type_param:
        supers = supers.filter(super_type__type=type_param)
        serializer = supersSerializer(supers, many = True)
        return Response(serializer.data)

    if request.method == 'GET':
        serializer = supersSerializer(supers, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = supersSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response (serializer.data, status = status.HTTP_201_CREATED)


@api_view(['GET','PUT', 'DELETE'])
def super_type_detail(request,pk):
    super = get_object_or_404(Supers,pk=pk)

    if request.method == 'GET':
        serializer = supersSerializer(super)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = supersSerializer(super, data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
        
    elif request.method == 'DELETE':
        super.delete()
        return Response (status = status.HTTP_204_NO_CONTENT)

    
    
    
    # super_type_param = request.query_params.get('supertype')
    # sort_param = request.query_params.get('sort')

    # supers = Supers.objects.all()

    # if super_type_param:
    #     supers = supers.filter(super_type_param=super_type_param)

    # if sort_param:
    #     supers = supers.order_by(sort_param)


    # serializer = supersSerializer(supers, many=True)

    # return Response(serializer.data)
