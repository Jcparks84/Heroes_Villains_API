from django.shortcuts import render


# @api_view(['GET','POST'])
# def supers_list(request):
#     supers_list = SuperType.objects.all()

#     if request.method == 'GET':
#         supers = Supers.objects.all()
#         serializer = supersSerializer(supers,many = True)
#         return Response(serializer.data)

#     elif request.method == 'POST':
#         serializer = supersSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response (serializer.data, status = status.HTTP_201_CREATED)


# @api_view(['GET','PUT', 'DELETE'])
# def super_type_detail(request,pk):
#     supers_details = get_object_or_404(Supers,pk=pk)
#     super_type = get_object_or_404(Supers, pk=pk)

#     if request.method == 'GET':
#         serializer = supersSerializer(super_type)
#         return Response(serializer.data)

#     elif request.method == 'PUT':
#         serializer = supersSerializer(super_type, data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data)
        
#     elif request.method == 'DELETE':
#         super_type.delete()

#         return Response (status = status.HTTP_204_NO_CONTENT)
# # Create your views here.
