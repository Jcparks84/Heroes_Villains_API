from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import supersSerializer
from Super_Type.serializers import SuperTypeSerializer
from .models import Supers


@api_view(['GET', 'POST'])
def supers_list(request):
    # if request.method == 'GET':
    #     supers = Supers.objects.all()
    #     serializer = supersSerializer(supers)
    
    super_type_param = request.query_params.get('supertype')
    sort_param = request.query_params.get('sort')

    supers = Supers.objects.all()

    if super_type_param:
        supers = supers.filter(super_type_param=super_type_param)

    if sort_param:
        supers = supers.order_by(sort_param)


    serializer = supersSerializer(supers, many=True)

    return Response(serializer.data)
