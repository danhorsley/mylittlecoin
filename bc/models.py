from django.db import models

class User(models.Model):
   
    id = models.IntegerField(primary_key=True)
    coins_received = models.CharField(max_length=15)
    coins_sent = models.CharField(max_length=15)
   
  
    

class Chain_DB(models.Model):
    
    index = models.IntegerField(primary_key=True)
    time = models.FloatField()
    cur_tran = models.CharField(max_length=250)
    proof = models.IntegerField()
    prev_hash = models.CharField(max_length=250)


class trdb(models.Model):
    """maintains the list of transactions in the form
    nt = {'sender' : sender, 'recipient' : recipient,
                 'amount' : amount, 'index' : self.chain[-1]['index']}"""
    id = models.IntegerField(primary_key=True)
    sender = models.CharField(max_length=250)
    recipient = models.CharField(max_length=250)
    amt = models.IntegerField()
    index = models.IntegerField()

    def __init__(self, sender, recipient, amt, index):
        self.id=time()
        self.sender = sender
        self.recipient = recipient
        self.amt = amt
        self.index = index

