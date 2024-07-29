from rest_framework.decorators import api_view
from rest_framework.response import Response
from home.models import Person
from home.serializers import PersonsSerializer


# @api_view(['GET', 'POST', 'PUT'])
# def index(request):

#     courses = {
#             'course_name' : 'Python',
#             'learn' : ['flask', 'Django', 'Tornado', 'FastApi'],
#             'course_provider' : 'George Kokkas'
#             }
    
#     if request.method == 'GET':
#         print('You hit a GET method')
#         print(request.GET.get('search'))
#         return Response(courses)
#     elif request.method == 'POST':
#         print('You hit a POST method')
#         data = request.data
#         print('******')
#         print(data['name'])
#         print('******')
#         return Response(courses)
#     elif request.method == 'PUT':
#         print('You hit a PUT method')
#         return Response(courses)

@api_view(['GET', 'POST'])
def index(request):

    if request.method == 'GET':
        json_response = {
            'name' : 'George',
            'courses': ['C++', 'Python'],
            'method': 'GET'
        }
    else:
        data = request.data
        print(data)
        json_response = {
            'name' : 'George',
            'courses': ['C++', 'Python'],
            'method': 'GET'
        }
    return Response(json_response)

@api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
def person(request, id=None):
    if request.method == 'GET':
        if id:
            try:
                obj = Person.objects.get(id=id)
                serializer = PersonsSerializer(obj)
                return Response(serializer.data)
            except Person.DoesNotExist:
                return Response({'error': 'Person not found'}, status=404)
        else:
            objs = Person.objects.all()
            serializer = PersonsSerializer(objs, many=True)
            return Response(serializer.data)
    
    elif request.method == 'POST':
        data = request.data
        serializer = PersonsSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        else:
            return Response(serializer.errors, status=400)
    
    elif request.method == 'PUT':
        if not id:
            return Response({'error': 'ID not provided'}, status=400)
        data = request.data
        try:
            obj = Person.objects.get(id=id)
        except Person.DoesNotExist:
            return Response({'error': 'Person not found'}, status=404)
        serializer = PersonsSerializer(obj, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=400)

    elif request.method == 'PATCH':
        if not id:
            return Response({'error': 'ID not provided'}, status=400)
        data = request.data
        try:
            obj = Person.objects.get(id=id)
        except Person.DoesNotExist:
            return Response({'error': 'Person not found'}, status=404)
        serializer = PersonsSerializer(obj, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=400)
    
    elif request.method == 'DELETE':
        if id is None:
            return Response({'error': 'ID not provided'}, status=400)
        try:
            obj = Person.objects.get(id = id)
            obj.delete()
            return Response({'message': 'person deleted'}, status=204)
        except Person.DoesNotExist:
            return Response({'error': 'Person not found'}, status=404)