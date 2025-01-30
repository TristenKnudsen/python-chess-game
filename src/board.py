from src.pieces import Pawn
class Board:
    def __init__(self):
       self.board = [[None for x in range(8)] for y in range(8)]
       self.setupPieces()
    def setupPieces(self):
        self.board[0] = ["R","N","B","Q","K","B","N","R"]
        for col in range(8): self.board[1][col] = Pawn("white")
        self.board[6] = ["p"]*8
        self.board[7] = ["r","n","b","q","k","b","n","r"]
    def printBoard(self):
        for c in self.board:
            formattedRow = [str(piece) if piece else "." for piece in c]
            print(" ".join(formattedRow))
            
    def getPiece(self, row:int, col:int) -> str |None:
        return self.board[row][col]
        
    def movePiece(self, startx:int,starty:int, endx:int, endy:int):
        self.board[endx][endy] = self.board[startx][starty]
        self.board[startx][starty] = None
        board.printBoard()
        
    def movePiece1(self, sx,sy, ex,ey):
        print(self.board[sx][sy].canMove(self.board, sx,sy, ex, ey))
        
    def addPiece(self,locX,locY):
        self.board[locX][locY] = "0"
    
    
        
board = Board()
board.movePiece1(1,0,3,0)
#print("\n")
#board.addPiece(3,2)
#board.movePiece(0,1,2,2)
