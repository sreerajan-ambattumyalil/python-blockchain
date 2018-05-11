import hashlib

def calculateHash(index, previousHash, timestamp, data):
    text = str(index) + previousHash + timestamp + data
    return hashlib.sha256(text.encode('utf-8')).digest()
    
