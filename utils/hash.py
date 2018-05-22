import hashlib
import sys
def calculateHash(index, previousHash, timestamp, data):
    text = str(index) + str(previousHash) + str(timestamp) + str(data)
    return str(hashlib.sha256(text.encode('utf-8')).digest())