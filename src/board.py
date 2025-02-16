from pieces import Pawn, King, Knight, Rook, Bishop, Queen
import copy

class Board:
    def __init__(self):
       self.board = [[None for x in range(8)] for y in range(8)]
       self.whitePieces = []
       self.blackPieces = []
       self.whiteKing = King(1, 0, 4)
       self.blackKing = King(-1, 3, 0)
       self.setupPieces()
       self.turnColour = 1


    def setupPieces(self):
        # Setting up White pieces
        #self.addPiece(Rook(1, 0, 0))
        #self.addPiece(Knight(1, 0, 1))
        #self.addPiece(Bishop(1, 0, 2))
        self.addPiece(Queen(1, 1, 1))
        self.addPiece(self.whiteKing)
        #self.addPiece(Bishop(1, 0, 5))
        #self.addPiece(Knight(1, 0, 6))
        self.addPiece(Rook(1, 7, 1))
        
        # Placing White Pawns
        #for col in range(8):
        #    self.addPiece(1, Pawn(1, 1, col))
        self.addPiece(Pawn(-1, 1, 0))
        
        # Setting up Black pieces
        #self.addPiece(Rook(-1, 7, 0))
        #self.addPiece(Knight(-1, 7, 1))
        #self.addPiece(Bishop(-1, 7, 2))
        #self.addPiece(Queen(-1, 7, 3))
        self.addPiece(self.blackKing)
        #self.addPiece(Bishop(-1, 7, 5))
        #self.addPiece(Knight(-1, 7, 6))
        #self.addPiece(Rook(-1, 7, 7))
        
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
    
    def getAllEnemyCapturableSquare(self, colour):
        capturable = []
        colourPieces = []
        
        if colour == 1:
            colourPieces = self.blackPieces
        else:
            colourPieces = self.whitePieces

        for piece in colourPieces:
            capturable.extend(piece.capturables(self))
                
        return capturable
        
    def getNumberOfMoves(self, colour):
        moves = 0
        colourPieces = []
        
        if colour == 1:
            colourPieces = self.whitePieces
        else:
            colourPieces = self.blackPieces
        
        for piece in colourPieces:
            moves += len(piece.moves(self))
            
        return moves
        
        
    
            
    def checkIfLegalMove(self, piece, eRow, eCol): #simulate the move on a copy of the board
        pieceColour = piece.colour
        sRow = piece.row
        sCol = piece.col
        #safe = True
        
        king = self.whiteKing if piece.colour == 1 else self.blackKing
        
        targetPiece = self.board[eRow][eCol]
        if targetPiece:
            (self.whitePieces if targetPiece.colour == 1 else self.blackPieces).remove(targetPiece)
        
        self.board[eRow][eCol] = self.board[sRow][sCol]
        self.board[sRow][sCol] = None
        piece.row = eRow
        piece.col = eCol
        
        newCapturables = self.getAllEnemyCapturableSquare(king.colour)
        kingPos = king.position()
        legal = kingPos not in newCapturables 
            
        self.board[sRow][sCol] = piece
        self.board[eRow][eCol] = targetPiece if targetPiece else None
        piece.row = sRow
        piece.col = sCol
        
        if targetPiece:
            (self.whitePieces if targetPiece.colour == 1 else self.blackPieces).append(targetPiece)
        
        return legal
        
       
    def movePiece(self, piece, eRow, eCol):
        pieceColour = piece.colour
        sRow = piece.row
        sCol = piece.col
        
        
        
        if eRow != "castle": #only king can have eRow "Castle"
            if self.checkIfLegalMove(piece, eRow,eCol):
                pass
            else:
                self.printBoardTesting()  
                return print("Illegal move! King in Check!")
        else:
            print("Castled",eCol)
            if eCol == "kingside":
                eRow , eCol = piece.row,6 #KING move square and row col
                self.executeMove(piece, eRow, eCol)
                
                #MOVE ROOK
                self.executeMove(self.board[eRow][7], eRow, 5)
                return
            if eCol == "queenside":
                eRow , eCol = piece.row,2 #KING move square and row col
                self.executeMove(piece, eRow, eCol)
                
                #MOVE ROOK
                self.executeMove(self.board[eRow][0], eRow, 3)
                return    
        
        if isinstance(piece, Pawn):
            print("moving piece is pawn")
            if [sRow + piece.colour, eCol] in piece.enPassantCaptures(self): 
                print("Move is enpassant move")
                #enPassantVictimPawn = self.board[sRow][eCol]
                self.board[piece.row][eCol] = None #remove enpassant pawn
                self.executeMove(piece, eRow, eCol)
                return
                  # Remove captured pawn
            if(2 - abs(sRow - eRow)  == 0):
                piece.potentialenPassant = True
            if eRow == 3.5 * (1 + piece.colour):
                #promote pawn
                promoteTo = input("PROMOTE PAWN: Queen, Rook, Bishop, Knight")
                pieceList = self.whitePieces if piece.colour == 1 else self.blackPieces
                
                pieceList.remove(piece)
                
                piece = globals()[promoteTo](piece.colour, piece.row, piece.col)
                
                pieceList.append(piece)
            
            
        
        
        target_piece = self.board[eRow][eCol] #pawns remove themself from the pieces
        if target_piece:
            if target_piece.colour == 1:
                self.whitePieces.remove(target_piece) #add to taken pieces
            else:
                self.blackPieces.remove(target_piece)
        
        self.turnColour *= -1
        self.executeMove(piece,eRow,eCol)
        #self.turnColour *= -1
    
    def executeMove(self, piece, eRow, eCol):
        sRow = piece.row
        sCol = piece.col
        self.board[eRow][eCol] = piece
        self.board[sRow][sCol] = None
        piece.row = eRow  
        piece.col = eCol
        piece.hasMoved = True
        self.printBoardTesting()
    
    def addPiece(self, piece):
        if piece.colour == 1:
            self.whitePieces.append(piece)
        else:
            self.blackPieces.append(piece)
            
        self.board[piece.row][piece.col] = piece
    
    def colourKingInCheck(self, colour):
        
        if colour == 1:
            colourKing = self.whiteKing
        else:
            colourKing = self.blackKing
           
        capturables = self.getAllEnemyCapturableSquare(colour)
        
        if colourKing.position() in capturables:
            return True
        else:
            return False
        

board1 = Board()

pieceRow = 0
pieceCol = 5


board1.printBoardTesting()
#turnColour = 1 #put into board class as variable, change when move is made *=-1
while True:
    turnColour = board1.turnColour
    
    if board1.getNumberOfMoves(turnColour) == 0:
        if board1.colourKingInCheck(turnColour):
            print("checkmate")
        else:
            print("Stalemate")
    
    if turnColour == 1:
        for piece in board1.whitePieces:
            if isinstance(piece, Pawn):
                    piece.potentialenPassant = False
    else:
        
        for piece in board1.blackPieces:
                if isinstance(piece, Pawn):
                        piece.potentialenPassant = False
    
    board1.blackKing.checkCastleMoves(board1)
    sRow, sCol = list(map(int,(input("Enter Piece coor: ").split(","))))
    piece = board1.getPiece(sRow,sCol)
    if piece is None:
        print("There is no piece on that square!")
    elif piece.colour != turnColour:
        print("Not your turn")
    elif len(piece.moves(board1)) == 0:
        print("This piece has no moves")
    else:
        q = 0
        for move in piece.moves(board1):
            print(str(q) + ":" + str(move))
            q += 1
            
        while True:
            try:
                userMoveNumber = int(input("Select move number: "))
                break  # Exit the loop if conversion is successful
            except ValueError or IndexError:
                print("Invalid input. Please enter a valid integer.")
        eRow,eCol = piece.moves(board1)[userMoveNumber]
        board1.movePiece(piece,eRow,eCol)
        turnColour *= -1
        