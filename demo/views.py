from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from demo.models import User 
from demo.models import Transaction 
from demo.serializers import UserSerializer
import json 

# Create your views here.

@csrf_exempt
def user_route(request):
    if request.method == 'GET':
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return JsonResponse(serializer.data, safe=False)
    if request.method == 'POST':
        data = json.loads(request.body)
        name = data.get("name")
        username = data.get("username")
        balance = data.get("balance")
        user = User.objects.create(name=name, username=username, balance=balance)
        serializer = UserSerializer(user, many = False)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data) 
        return JsonResponse(serializer.errors)
    
@csrf_exempt
def transaction_route(request):
    if request.method == 'GET':
        userid = request.GET.get('userid')
        user = User.objects.get(id = userid)
        send = Transaction.objects.filter(senderid = user)
        receive = Transaction.objects.filter(receiverid = user)
        transactions = list(send) + list(receive)
        # - ID (primary key)
        # - amount (float)
        # - sender id (foreign key)
        # - receiver id (foreign key)
        # - pending (boolean)
        data = { "id": transactions.id, "amount": transactions.amount, "sender": transactions.senderid.id, "receiver": transactions.receiverid.id, "pending": transactions.pending}
    return JsonResponse(data, safe = False)



