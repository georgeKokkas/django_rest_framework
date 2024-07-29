from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET', 'POST', 'PUT'])
def index(request):

    courses = {
            'course_name' : 'Python',
            'learn' : ['flask', 'Django', 'Tornado', 'FastApi'],
            'course_provider' : 'George Kokkas'
            }
    
    if request.method == 'GET':
        print('You hit a GET method')
        print(request.GET.get('search'))
        return Response(courses)
    elif request.method == 'POST':
        print('You hit a POST method')
        data = request.data
        print('******')
        print(data['name'])
        print('******')
        return Response(courses)
    elif request.method == 'PUT':
        print('You hit a PUT method')
        return Response(courses)
