from model.block import Block
from model.validation_response import ValidationResponse

class BlockValidator:
    def validate(self, newBlock : Block, previousBlock : Block):
        if(previousBlock.index + 1 != newBlock.index):            
            return ValidationResponse(False, "Index mismatch")
        if(newBlock.previousHash != previousBlock.hash):
            return ValidationResponse(False, "Hash mismatch")
        if()            
        return True
