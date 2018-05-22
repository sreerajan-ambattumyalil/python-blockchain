from model.block import Block
from model.block_chain import BlockChain
from utils.hash import calculateHash
import datetime
from flask import Flask
from flask import Response
from data.data_access import initialize_database
from flask import jsonify
from flask import request

app = Flask(__name__)

initialize_database()
block_chain = BlockChain()

@app.route('/')
def index():
    return "Hello World"

@app.route('/block_chain')
def get_block_chain():
    result = list(map(lambda block : block.__dict__, block_chain.blocks))
    print(jsonify(result))
    return jsonify(result)

@app.route('/block_chain', methods = ["POST"])
def add_block():
    data = request.args.get("data")
    previous_block = block_chain.getlatestBlock()
    index = previous_block.index + 1
    time_stamp = str(datetime.datetime.now())
    previous_hash = previous_block.hash
    block = Block(index, time_stamp, calculateHash(index, previous_hash, time_stamp, data) ,previous_hash, data)
    block_chain.addBlock(block)
    return jsonify({"status" : "Success"})


    
# def generateNextBlock(latestBlock : Block, data):
#     nextIndex = latestBlock.index
#     timestamp = datetime.datetime.now()
#     return Block(nextIndex, timestamp, latestBlock.hash, data)




