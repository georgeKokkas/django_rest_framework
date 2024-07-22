from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET', 'POST'])
def index(request):

    courses = {
            'course_name' : 'Python',
            'learn' : ['flask', 'Django', 'Tornado', 'FastApi'],
            'course_provider' : 'George Kokkas'
            }
    
    if request.method == 'GET':
        print('You hit a GET method')
        return Response(courses)
    elif request.method == 'POST':
        print('You hit a POST method')
        return Response(courses)
    
