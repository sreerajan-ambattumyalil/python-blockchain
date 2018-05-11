from model.block import Block
from model.block_chain import BlockChain
from utils.hash import calculateHash
import datetime

def generateNextBlock(latestBlock : Block, data):
    nextIndex = latestBlock.index
    timestamp = datetime.datetime.now()
    return Block(nextIndex, timestamp, latestBlock.hash, data)


blockChain = BlockChain()

generateNextBlock(blockChain.getlatestBlock(), "One")

print(block.toString())
print(calculateHash(1, "123", "456", "Srees data"))


