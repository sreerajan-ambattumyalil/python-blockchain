import hashlib
from utils.hash import calculateHash

class Block:

    def __init__(self, index, timestamp, previousHash, data):
        self.index = index
        self.timestamp = timestamp
        self.hash = calculateHash(index, previousHash, timestamp, data)
        self.previousHash = previousHash
        self.data = data

    def toString(self):
        return str(self.index) + str(self.timestamp) + str(self.hash) + str(self.previousHash) + str(self.data)
