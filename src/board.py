from pieces import Pawn, King, Knight, Rook, Bishop, Queen
import copy

class Board:
    def __init__(self):
       self.board = [[None for x in range(8)] for y in range(8)]
       self.whitePieces = []
       self.blackPieces = []
       self.whiteKing = King(1, 0, 4)
       self.blackKing = King(-1, 7, 4)
       self.setupPieces()


    def setupPieces(self):
        # Setting up White pieces
        self.addPiece(1, Rook(1, 0, 0))
        self.addPiece(1, Knight(1, 0, 1))
        self.addPiece(1, Bishop(1, 0, 2))
        self.addPiece(1, Queen(1, 0, 3))
        self.addPiece(1, self.whiteKing)
        self.addPiece(1, Bishop(1, 0, 5))
        self.addPiece(1, Knight(1, 0, 6))
        self.addPiece(1, Rook(1, 0, 7))
        
        # Placing White Pawns
        #for col in range(8):
        #    self.addPiece(1, Pawn(1, 1, col))
        
        # Setting up Black pieces
        self.addPiece(-1, Rook(-1, 7, 0))
        self.addPiece(-1, Knight(-1, 7, 1))
        self.addPiece(-1, Bishop(-1, 7, 2))
        self.addPiece(-1, Queen(-1, 7, 3))
        self.addPiece(-1, self.blackKing)
        self.addPiece(-1, Bishop(-1, 7, 5))
        self.addPiece(-1, Knight(-1, 7, 6))
        self.addPiece(-1, Rook(-1, 7, 7))
        
        # Placing Black Pawns
        #for col in range(8):
        #    self.addPiece(-1, Pawn(-1, 6, col))

        
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
    
    def printBoardTesting(self):
        for row_num, c in enumerate(self.board[::-1], start=1): 
            formattedRow = [str(piece) if piece else "." for piece in c]
            print(f"{8 - row_num} {' '.join(formattedRow)}")        
        print("  0 1 2 3 4 5 6 7")   
        
    def getPiece(self, row:int, col:int) -> str |None:
        return self.board[row][col]
    
    def getAllEnemyCapturableSquare(self, colour, board):
        capturable = []
        colourPieces = []
        
        if colour == 1:
            colourPieces = board.blackPieces
        else:
            colourPieces = board.whitePieces

        for piece in colourPieces:
            capturable.extend(piece.capturables(board))
                
        return capturable
    
    def inBounds(row, col): #returns bool
        return 0 <= row <= 7 and 0 <= col <= 7
       
    def checkIfLegalMove(self, piece, eRow, eCol):
        kingCheckBoard = copy.deepcopy(self)  
        pieceColour = piece.colour
        sRow = piece.row
        sCol = piece.col
        
        if pieceColour == 1:
            colourKing = kingCheckBoard.whiteKing
        else:
            colourKing = kingCheckBoard.blackKing
            
        faketarget_piece = kingCheckBoard.board[eRow][eCol]
        if faketarget_piece:
            if faketarget_piece.colour == 1:
                kingCheckBoard.whitePieces.remove(faketarget_piece) 
            else:
                kingCheckBoard.blackPieces.remove(faketarget_piece)
        
        kingCheckBoard.board[eRow][eCol] = kingCheckBoard.board[sRow][sCol]
        kingCheckBoard.board[sRow][sCol] = None
        kingCheckBoard.board[eRow][eCol].row = eRow  
        kingCheckBoard.board[eRow][eCol].col = eCol
        
        newCapturables = kingCheckBoard.getAllEnemyCapturableSquare(colourKing.colour, kingCheckBoard)
        kingPos = colourKing.position()
        
        if kingPos in newCapturables:
            return False
        else:
            return True
       
    def movePiece(self, piece, eRow, eCol):
        pieceColour = piece.colour
        sRow = piece.row
        sCol = piece.col
        if self.checkIfLegalMove(piece, eRow,eCol):
            pass
        else:
            self.printBoardTesting()  
            return print("Illegal move! King can be captured!")
        
        
        
        target_piece = self.board[eRow][eCol]
        if target_piece:
            if target_piece.colour == 1:
                self.whitePieces.remove(target_piece) #add to taken pieces
            else:
                self.blackPieces.remove(target_piece)
        self.board[eRow][eCol] = self.board[sRow][sCol]
        self.board[sRow][sCol] = None
        self.board[eRow][eCol].row = eRow  
        self.board[eRow][eCol].col = eCol
        self.printBoardTesting()  
    
    
    def addPiece(self,colour,piece):
        if colour == 1:
            self.whitePieces.append(piece)
        elif colour == -1:
            self.blackPieces.append(piece)
            
        self.board[piece.row][piece.col] = piece
#create list to hold white pieces and black pieces

board1 = Board()

pieceRow = 0
pieceCol = 5


board1.printBoardTesting()
print(board1.whiteKing.position())

while True:
    sRow, sCol = list(map(int,(input("Enter Piece coor: ").split(","))))
    
    piece = board1.getPiece(sRow,sCol)
    #print(len(piece.moves()))
    if piece is None:
        print("There is no piece on that square!")
    elif len(piece.moves(board1)) == 0:
        print("This piece has no moves")
    else:
        q=0
        for move in piece.moves(board1):
            print(str(0 + q) + ":" + str(move))
            q += 1
            
        while True:
            try:
                userMoveNumber = int(input("Select move number: "))
                break  # Exit the loop if conversion is successful
            except ValueError or IndexError:
                print("Invalid input. Please enter a valid integer.")
        #userMoveNumber = int(input("select move number"))
        eRow,eCol = piece.moves(board1)[userMoveNumber]
        board1.movePiece(piece,eRow,eCol)
        
        