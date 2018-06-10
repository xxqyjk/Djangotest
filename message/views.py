#_*_coding:utf-8_*_
from django.shortcuts import render
import MySQLdb

from .models import UserMessage

# Create your views here.

def getform(request):
    # all_messages = UserMessage.objects.all()
    all_messages = UserMessage.objects.filter(name="bobbytest")
    if all_messages:
        message = all_messages[0]

    # all_messages = UserMessage.objects.filter(name="bobby", address='北京')
    # all_messages.delete()
    for message in all_messages:
        message.delete()
        # print message.name

    # if request.method == 'POST':
    #     name = request.POST.get('name','')
    #     message = request.POST.get('message', '')
    #     email = request.POST.get('email', '')
    #     address = request.POST.get('address', '')
    #     user_message = UserMessage()
    #     user_message.name = name
    #     user_message.message = message
    #     user_message.address = address
    #     user_message.email = email
    #     user_message.object_id = "helloworld3"
    #     user_message.save()

    return render(request, 'message_form.html')
