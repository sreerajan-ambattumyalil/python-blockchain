import hashlib
from model.block import Block

def calculateHash(index, previousHash, timestamp, data):
    text = str(index) + previousHash + timestamp + data
    return hashlib.sha256(text.encode('utf-8')).digest()

def calculateHashForBlock(block : Block):
    data = str(block.index) + block.previousHash + block.timestamp + block.data
    return hashlib.sha256(data.encode('utf-8'))
    
