import hashlib
import requests

import sys


# TODO: Implement functionality to search for a proof 

def proof_of_work(previous_proof):

    # Truth be told, I took much of this from blockchain.py
    # Do not need self since we're not calling a class here
    proof = 0
    while valid_proof(previous_proof, proof) is False:
        proof += 1  # If the first # doesn't work, check the next one
    return proof


def valid_proof(previous_proof):
    guess = f'{previous_proof}{proof}'.encode()  # needs encoding to make it work
    guess_hash = hashlib.sha256(guess).hexdigest() # hash the guess

    # have to change this back to six zeros
    return guess_hash[:3] == "000"



if __name__ == '__main__':
    # What node are we interacting with?
    if len(sys.argv) > 1:
        node = sys.argv[1]
    else:
        node = "http://localhost:5000"

    coins_mined = 0
    # Run forever until interrupted
    while True:
        # TODO: Get the last proof from the server and look for a new one
        # keeping this source for future reference https://www.geeksforgeeks.org/               get-post-requests-using-python/
        response = requests.get('localhost:5000/proof')
        data = response.json()
        previous_proof = data['proof']
        # TODO: When found, POST it to the server {"proof": new_proof}
        # I don't understand this.  Wouldn't it be
        new_proof = proof_of_work(previous_proof)
        # TODO: We're going to have to research how to do a POST in Python
        # HINT: Research `requests` and remember we're sending our data as JSON
        # source https://www.w3schools.com/python/showpython.asp?filename=demo_requests_post
        send_it_out = {}
        r = requests.post(url = API_ENDPOINT, data = data)
        # TODO: If the server responds with 'New Block Forged'
        # add 1 to the number of coins mined and print it.  Otherwise,
        # print the message from the server.
        pass
