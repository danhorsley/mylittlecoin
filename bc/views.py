from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import requests
from django.http import HttpResponse, JsonResponse
from .models import *
from .blockchain import *
from .miner import *
import secrets
from decouple import config
import json

node = 'http://127.0.0.1:7000'
blockchain = Blockchain()

# Create your views here.


def basic(request):
    return render(request, 'basic.html')

def wallet(request):
    return render(request, 'wallet.html')

def deephash(request):
    if request.method == 'POST':
        my_id= config('MINER_1_ID')
        last_block = requests.get(node + '/last_block').json()
        my_proof = proof_of_work(last_block)
        post_proof = requests.post(node + '/mine',{'proof' : my_proof, "id" : my_id}).json()
        return render(request, 'deephash.html', {'mined': post_proof})
    else:
        post_proof = {'no coins mined so far'}
        return render(request,'deephash.html', {'mined': post_proof})
        

def last_block(request):
    return JsonResponse(blockchain.chain[-1])

@csrf_exempt
def mine(request):
    # format  - post_data = {'proof': str(new_proof), 'id': id}
    if request.method == 'POST':
        last_block_string = json.dumps(blockchain.chain[-1], sort_keys=True)
        if blockchain.valid_proof(last_block_string, request.POST['proof']):
            blockchain.new_block(request.POST['proof'], blockchain.hash(blockchain.chain[-1]))
            blockchain.new_transaction(config('COIN_CORE'), request.POST['id'], 1)
            return JsonResponse({'new block mined by': request.POST['id']})
        else:
            return JsonResponse({'not a proof by id : ': request.POST['id']})
    else:
        return JsonResponse({'last_block': blockchain.chain[-1]})

def new_user(request):
    if request.method == 'POST':
        my_new_user_id = secrets.token_hex(16)
        new_user = User(id = my_new_user_id)
        new_user.save()
        return JsonResponse({'new user id' : my_new_user_id})
    else:
        return render(request,'new_user.html')

