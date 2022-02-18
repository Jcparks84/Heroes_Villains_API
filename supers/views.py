from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import HeroesVillainsSerializer
from .models import HeroesVillains


@api_view(['GET'])
def heroes_villains_list(request):
    
    super_type_param = request.query_params.get('supertype')
    sort_param = request.query_params.get('sort')

    supers = HeroesVillains.objects.all()

    if super_type_param:
        supers = supers.filter(super_type_param=super_type_param)

    if sort_param:
        supers = supers.order_by(sort_param)


    serializer = HeroesVillainsSerializer(supers, many=True)

    return Response(serializer.data)
