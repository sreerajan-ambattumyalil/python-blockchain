from pydblite import Base
from datetime import datetime
from model.block import Block
from model.block_chain import BlockChain
from utils.hash import calculateHash

def initialize_database():
    print("Initializing database!")
    db = Base('block_chain.pdl')
    if(db.exists()):
        print("Delete block chain database")
        db.delete
    db.create('index', 'timestamp', 'hash', 'previousHash', 'data', mode="override")
    genesisData = "It all begins here!"
    timestamp = datetime.now()
    index = 0
    hash = calculateHash(index, "", timestamp, genesisData)
    genesisBlock = Block(index, str(timestamp), hash, None, genesisData)
    db.insert(genesisBlock.index, genesisBlock.timestamp, genesisBlock.hash, genesisBlock.previousHash, genesisBlock.data)
    db.commit()

