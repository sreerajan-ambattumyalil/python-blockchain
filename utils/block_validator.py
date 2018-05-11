from model.block import Block
from model.validation_response import ValidationResponse
from utils.hash import calculateHashForBlock
import datetime

class BlockValidator:

    def __validStructure(self, block : Block):
        if(isinstance(block.index, int) and isinstance(block.timestamp, datetime.datetime) and isinstance(block.previousHash, bytes) and isinstance(block.data, str)):
            return True
        return False

    def validate(self, newBlock : Block, previousBlock : Block):
        if(previousBlock.index + 1 != newBlock.index):            
            return ValidationResponse(False, "Index mismatch")
        if(newBlock.previousHash != previousBlock.hash):
            return ValidationResponse(False, "Hash mismatch")
        if(calculateHashForBlock(newBlock) != newBlock.hash):
            return ValidationResponse(False, "Hash mismatch")
        if(not (self.__validStructure(newBlock))):
            return ValidationResponse(False, "Invalid structure")
        return ValidationResponse(True, "Valid Block")
