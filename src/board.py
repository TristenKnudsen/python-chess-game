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
    def printBoardBlack(self):
        for row_num, c in enumerate(self.board, start=1): 
            formattedRow = [str(piece) if piece else "." for piece in c[::-1]]
            print(f"{row_num} {' '.join(formattedRow)}")  
        print("  " + "a b c d e f g h"[::-1])               
        
        
    def printBoardWhite(self):
        for row_num, c in enumerate(self.board[::-1], start=1): 
            formattedRow = [str(piece) if piece else "." for piece in c]
            print(f"{9 - row_num} {' '.join(formattedRow)}")        
        print("  a b c d e f g h")   
            
    def getPiece(self, row:int, col:int) -> str |None:
        return self.board[row][col]
    
    def inBounds(row, col):
        return 0 <= row <= 7 and 0 <= col <= 7
        
    #def movePiece(self, startx:int,starty:int, endx:int, endy:int):
    #    self.board[endx][endy] = self.board[startx][starty]
    #    self.board[startx][starty] = None
    #    board.printBoard()
        
    def movePiece(self, piece, move):
        if isinstance(piece, Pawn):
            print("The piece is a Pawn!")
        else:
            print("The piece is not a Pawn.")
        row, col = move
        self.board[row][col] = piece
        self.board[piece.row][piece.col] = None
        piece.row = row
        piece.col = col
    
    
        
    #def movePiece1(self, sx,sy, ex,ey):
    #    print(self.board[sx][sy].canMove(self.board, sx,sy, ex, ey))
        
    def addPiece(self,piece):
        self.board[piece.row][piece.col] = piece
    
    
#create list to hold white pieces and black pieces

board = Board()
board.addPiece(Pawn(1,2,1))
print("\n WHITE VIEW\n")
board.printBoardWhite();
print("\n BLACK VIEW\n")
board.printBoardBlack();



#move = input("Enter move: ")
#example moves; pe4, Nf3, Nc3, be6, 
#work on move translator



#Go through every piece that white has, put them all into this moves list
#translate the moves list to chess notation
#check if the move the user entered exists in the list, if so make the move, if not say invalid
#moves = board.getPiece(pieceRow,pieceCol).moves(board.board)

#BETTER WAY TO DO COORDINATE SYSTEM WHERE MOVES ARE SEEN 


print(board.getPiece(2,1).moves(board.board))
