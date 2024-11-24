from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from demo.models import User
from demo.serializers import UserSerializer

# Create your views here.

@csrf_exempt
def user_route(request):
    if request.method == 'GET':
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return JsonResponse(serializer.data, safe=False)
    if request.method == 'POST':
        # TODO: Implement creating a new user
        pass
    
@csrf_exempt
def transaction_route(request):
    # TODO: EXTRA CREDIT: Get all of a user's transactions
    pass