from django.http import Http404
from django.http import HttpResponse
from django.shortcuts import render
from django.core import serializers
from blockchainex.models import Block
from blockchainex.connectRemote import ConnectRemote
import json

def home(request):
    return HttpResponse("Home")

def about(request):
    return HttpResponse("About")

def block(request, block):
    context = []

    try:
        res = Block.objects.get(hash=block)
    except Block.DoesNotExist:
        # raise Http404("tratata")
        c = ConnectRemote()

        block = c.runCommand("GET-BLOCK-BY-HASH", block)
        res = json.loads(block)

        print(res)
        block = Block(hash=res[0]["hash"])
        resa = vars(block)
        print(resa)

        context = {
            'oneBlock': [resa]
        }

    return render(request, 'blockchainex/block.html', context)