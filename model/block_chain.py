from model.block import Block
import datetime

class BlockChain:
    def __init__(self):
        genesisBlock = Block(0, str(datetime.datetime.now()), None, "It all begins here!")
        self.blocks = [genesisBlock]
        self.latesBlock = genesisBlock

    def getlatestBlock(self):
        return self.latesBlock

    def addBlock(self, block):
        self.blocks.append(block)
        self.latesBlock = block
    
    def getBlocks(self):
        return self.blocks