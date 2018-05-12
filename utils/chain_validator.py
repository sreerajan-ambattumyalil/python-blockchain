from model.block_chain import BlockChain
from model.validation_response import ValidationResponse
from utils.block_validator import BlockValidator
from model.block import Block

class ChainValidator:
    def __init__(self, blockValidator : BlockValidator):
        self.blockValidator = blockValidator
    
    def validate(self, blocks : list):

        for index in range(1, len(blocks)):
            if(not self.blockValidator.validate(blocks[index], blocks[index - 1])):
                return ValidationResponse(False, "Invalid chain")
        return ValidationResponse(True, "Valid Chain")