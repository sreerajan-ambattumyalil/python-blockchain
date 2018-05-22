from model.block import Block
import datetime
from model.repository_base import Repository

class BlockChain(Repository):
    def __init__(self):
        super().__init__()
        for rec in self.db:
            self.blocks = []
            block = Block(rec['index'], rec['timestamp'], rec['hash'], rec['previousHash'], rec['data'])
            self.blocks.append(block)

    def getlatestBlock(self):
        return sorted(self.blocks, key=lambda x : x.index, reverse=True)[0]

    def addBlock(self, block):
        self.blocks.append(block)
        self.db.insert(block.index, block.timestamp, block.hash, block.previousHash, block.data)
    
    def getGenesisBlock(self):
        return next(block for block in self.blocks if block.index == 0)