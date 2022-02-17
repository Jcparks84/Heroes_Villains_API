from rest_framework.decorators import api_view
from rest_framework.response import Response
from Super_Type.models import SuperType


@api_view(['GET'])
def heroes_villains_list(request):

    return Response('ok')
