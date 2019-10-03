#### What is a block chain?
* Immutable
* Impossible to delete things
* Built on proof rather than trust
* Hash connects the blocks.  Change the hash, it breaks the chain
* A proof is a special number.
* SHA-256 will be used for hashing

#### What does a hashing function do?
* Predictable output
* Random, but not truly random
* Deterministic
* Secure.  
* Uniform distribution.  
* What do we need for the proof to be valid?  

At command line: pipenv install    
At command line: pipenv shell

* What is hashlib?  Has to do with hash algorithms.
* UUID is for generating unique id's
* What is flask?  A web framework

* A set in Python is an array of unique values.  It's O(1).

* self.new_block.  what does the previous_hash=1 mean?  This is the genesis block.  Why is one a good value for the previous hash?  You'll know it's artificial. 

* what is @staticmethod?  It's a decorator.  They are ways to assigning properties to a method.  This is a static method.  Static means it doesn't change. It can be called w/o the class existence.  

* block_string = json.dumps(block, sort_keys=True).encode().  What is this?  This is like stringify and parse.  You can send it via a web api.  look up .encode  Where is it being used?  The hash library is using the encoded block string.  
* Using string's encode() method, you can convert unicoded strings into any encodings supported by Python

* What is hexdigest?  It's used for hex-encoding a string.  We want this for proof of work.  Makes sure the string has the right character encoding for what sha-256 is looking for.

* @property lets you create a property in an object. 

* What is while current_index < len(chain) looping through?  The entire chain.

* How to run on port 5000?  python3 blockchain.py

## Notes for October 3

* Consensus in blockchain is about agreement in the next block

