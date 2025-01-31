from pieces import Pawn

class Board:
    def __init__(self):
       self.board = [[None for x in range(8)] for y in range(8)]
       #self.setupPieces()
    #def setupPieces(self):
        #self.board[0] = ["R","N","B","Q","K","B","N","R"]
        #for col in range(8): self.board[1][col] = Pawn("white",1,col)
        #self.board[6] = ["p"]*8
        #self.board[7] = ["r","n","b","q","k","b","n","r"]
    def printBoard(self):
        for c in self.board:
            formattedRow = [str(piece) if piece else "." for piece in c]
            print(" ".join(formattedRow))
            
    def getPiece(self, row:int, col:int) -> str |None:
        return self.board[row][col]
    
    def inBounds(row, col):
        return 0 <= row <= 7 and 0 <= col <= 7
        
    def movePiece(self, startx:int,starty:int, endx:int, endy:int):
        self.board[endx][endy] = self.board[startx][starty]
        self.board[startx][starty] = None
        board.printBoard()
    
        
    #def movePiece1(self, sx,sy, ex,ey):
    #    print(self.board[sx][sy].canMove(self.board, sx,sy, ex, ey))
        
    def addPiece(self,piece):
        self.board[piece.row][piece.col] = piece
    
    
#create list to hold white pieces and black pieces

board = Board()
board.addPiece(Pawn(-1,5,5))
board.addPiece(Pawn(-1,5,4))
board.addPiece(Pawn(1,5,6))
board.getPiece(5,4).potentialenPassant = True


#board.addPiece(Pawn(-1,1,2))
#board.addPiece(Pawn(-1,1,0))
#board.getPiece(1,2).enPassant = True;
#board.getPiece(1,0).enPassant = False;

#board.addPiece(Pawn(-1,2,1))
#board.addPiece(Pawn(-1,2,2))
#board.addPiece(Pawn(1,3,1))
#board.addPiece(Pawn(-1,1,0))
board.printBoard();
print(board.getPiece(5,5).moves(board.board))
#board.movePiece1(1,0,3,0)
#print("\n")
#board.addPiece(3,2)
#board.movePiece(0,1,2,2)
