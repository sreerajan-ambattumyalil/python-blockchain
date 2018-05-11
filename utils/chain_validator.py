from model.block_chain import BlockChain
from model.validation_response import ValidationResponse

class ChainValidator:
    def validate(self, blockchain : BlockChain):
        return ValidationResponse(True, "Valid Chain")