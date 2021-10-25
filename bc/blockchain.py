import hashlib
import json
from time import time
from uuid import uuid4
import requests
from .models import *

class Blockchain(object):
    def __init__(self):
        self.chain = []
        self.current_transactions = []
        self.difficulty = 3
        
        self.new_block(previous_hash=1, proof=100) #genesis block

    def new_block(self, proof, previous_hash=None):
        block = {'index' : len(self.chain) + 1, 'time' : time(),
        'current_transactions' : [], 'proof' : proof, 
        'previous_hash' : previous_hash}
        self.current_transactions = []
        self.chain.append(block)

        return block

    def hash(self,block):
        block = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha224(block).hexdigest()
    
    def valid_proof(self,block_string, proof):
        new_string = (block_string + str(proof)).encode()
        hash_try=hashlib.sha256(new_string).hexdigest()
        return hash_try[:self.difficulty] == '0' * self.difficulty
    
    def new_transaction(self, sender, recipient, amount):
        nt = {'sender' : sender, 'recipient' : recipient,
                 'amount' : amount, 'index' : self.chain[-1]['index']}
        self.current_transactions.append(nt)
        new_db_transaction = trdb(sender = nt['sender'],
                                        recipient = nt['recipient'],
                                        amt = nt['amount'],
                                        index = nt['index'])
        new_db_transaction.save()   
        