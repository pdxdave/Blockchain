import hashlib
import requests

import sys


# TODO: Implement functionality to search for a proof 

def proof_of_work(previous_proof):
    # Truth be told, I took much of this from blockchain.py
    proof = 0
    while valid_proof(previous_proof, proof) is False:
        proof += 1  # If the first # doesn't work, check the next one
    return proof


def valid_proof(previous_proof, proof):
    guess = f'{previous_proof}{proof}'.encode()  # needs encoding to make it work
    guess_hash = hashlib.sha256(guess).hexdigest() # hash the guess

    # have to change this back to six zeros
    return guess_hash[:6] == "000000"



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
        # keeping this source for future reference https://www.geeksforgeeks.org/get-post-requests-using-python/
        response = requests.get("http://localhost:5000/last_block")
        data = response.json()
        previous_proof = data['proof']
        # TODO: When found, POST it to the server {"proof": new_proof}
        # I don't understand this.  Wouldn't it be
        new_proof = proof_of_work(previous_proof)
        # TODO: We're going to have to research how to do a POST in Python
        # HINT: Research `requests` and remember we're sending our data as JSON
        # source https://www.w3schools.com/python/showpython.asp?filename=demo_requests_post
        # adding a name is a last minute change. didn't realize this until I got to blockchain.py
        send_it_out = {'proof': new_proof, 'recipient': 'Nigel Tufnel'}
        r = requests.post("http://localhost:5000/mine", json=send_it_out)
        # TODO: If the server responds with 'New Block Forged'
        # add 1 to the number of coins mined and print it.  Otherwise,
        # print the message from the server.
        # Taking a leap here based on the wording. 'If' suggests an if statement
        # and server responds suggests it has to pass a status code.
        # https://www.restapitutorial.com/httpstatuscodes.html
        if r.status_code is 201:
            print("Coin")
            coins_mined += 1
            print("Your coin count is: ", coins_mined)

