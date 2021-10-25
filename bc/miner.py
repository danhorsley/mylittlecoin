import json
import hashlib

def proof_of_work(block):

    stringify = json.dumps(block, sort_keys = True)
    proof_guess = 0
    while valid_proof(stringify, proof_guess) is False:
        proof_guess += 1
        
    return proof_guess

def valid_proof(block_string, proof):

    new_string = (block_string + str(proof)).encode()
    hash_try = hashlib.sha256(new_string).hexdigest()

    return hash_try[:3] == '000'