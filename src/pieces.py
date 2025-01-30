class Piece:
    def __init__(self, colour: str):
        self.colour = colour
        self.symbol = ""
        self.hasMoved = False

class Pawn(Piece):
    def __init__(self,colour):
        super().__init__(colour)
        self.symbol = "P"
    def __repr__(self):
        return self.symbol.upper() if self.colour == "white" else self.symbol.lower()
        
    def canMove(self,board,sx,sy, ex,ey):
        if (sy == ey) and ey == (sy +1) or ey == (sy+2):
            return True
        else:
            return False
            
    
