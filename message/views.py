#_*_coding:utf-8_*_
from django.shortcuts import render
import MySQLdb

from .models import UserMessage

# Create your views here.

def getform(request):
    message = None
    all_messages = UserMessage.objects.filter(name="bobby")
    if all_messages:
        message = all_messages[0]

    return render(request, 'message_form.html', {
        "my_message":message
    })
