import hashlib
from utils.hash import calculateHash

class Block:

    def __init__(self, index, timestamp, hash, previousHash, data):
        self.index = index
        self.timestamp = timestamp
        self.hash = hash
        self.previousHash = previousHash
        self.data = data

    def toString(self):
        return str(self.index) + str(self.timestamp) + str(self.hash) + str(self.previousHash) + str(self.data)
