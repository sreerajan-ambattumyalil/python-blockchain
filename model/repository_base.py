from pydblite import Base

class Repository:
    def __init__(self):
        db = Base('block_chain.pdl')
        db.open()
        self.db = db 
