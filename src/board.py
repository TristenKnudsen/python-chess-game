class Board:
    def __init__(self):
       self.board = [[None for x in range(8)] for y in range(8)]
       self.setupPieces()
    def setupPieces(self):
        self.board[0] = ["R","N","B","Q","K","B","N","R"]
        self.board[1] = ["P"]*8
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
    
    
        
board = Board()
board.movePiece(1,0,2,0)
print("\n")
board.movePiece(0,1,2,2)
