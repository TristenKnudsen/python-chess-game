from pieces import Pawn, King, Knight, Rook, Bishop, Queen

class Board:
    def __init__(self):
       self.board = [[None for x in range(8)] for y in range(8)]
       self.whitePieces = []
       self.blackPieces = []
       self.setupPieces()
       

    def setupPieces(self):
        # Setting up White pieces
        self.addPiece(1, Rook(1, 0, 0))
        self.addPiece(1, Knight(1, 0, 1))
        self.addPiece(1, Bishop(1, 0, 2))
        self.addPiece(1, Queen(1, 0, 3))
        self.addPiece(1, King(1, 0, 4))
        self.addPiece(1, Bishop(1, 0, 5))
        self.addPiece(1, Knight(1, 0, 6))
        self.addPiece(1, Rook(1, 0, 7))
        
        # Placing White Pawns
        for col in range(8):
            self.addPiece(1, Pawn(1, 1, col))
        
        # Setting up Black pieces
        self.addPiece(-1, Rook(-1, 7, 0))
        self.addPiece(-1, Knight(-1, 7, 1))
        self.addPiece(-1, Bishop(-1, 7, 2))
        self.addPiece(-1, Queen(-1, 7, 3))
        self.addPiece(-1, King(-1, 7, 4))
        self.addPiece(-1, Bishop(-1, 7, 5))
        self.addPiece(-1, Knight(-1, 7, 6))
        self.addPiece(-1, Rook(-1, 7, 7))
        
        # Placing Black Pawns
        for col in range(8):
            self.addPiece(-1, Pawn(-1, 6, col))

        
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
            colourPieces = self.blackPieces
        else:
            colourPieces = self.whitePieces

        for piece in colourPieces:
            capturable.extend(piece.capturables(board))
                
        return capturable
    
    def inBounds(row, col): #returns bool
        return 0 <= row <= 7 and 0 <= col <= 7
        
    def movePiece(self, sRow:int,sCol:int, eRow:int, eCol:int):
        target_piece = self.board[eRow][eCol]
        if target_piece:
            if target_piece.colour == 1:
                self.whitePieces.remove(target_piece)
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




#board1.addPiece(1,Pawn(1,7,6))
#board1.addPiece(-1,King(-1,3,4))
#board1.addPiece(1,Bishop(1,5,2))
#board1.addPiece(1,Bishop(1,5,2))

#board1.addPiece(1,Rook(1,0,4))
#board1.addPiece(1,Rook(1,0,3))

#board1.addPiece(1,Knight(1,0,6))

#print(len(board1.getPiece(5,2).capturables(board1)))
#for piece in board1.whitePieces:
 #   print("# moves of Piece: ", piece, " : ", len(piece.moves(board1)))
#board1.addPiece(-1,Pawn(-1,4,2))
#board1.addPiece(-1,Queen(-1,4,1))
#board1.addPiece(1,King(1,3,3))
#print(board1.getAllEnemyCapturableSquare(1))



#print("# of King moves: " + str(len(board1.getPiece(3,4).moves(board1))))
#print("King moves: " + str(board1.getPiece(3,4).moves(board1)))
#print("King moves:")
#print(board1.getPiece(3,4).moves(board1))

#print("# of enemy queen moves" + str(len(board1.getPiece(4,1).moves(board1))))


board1.printBoardTesting()

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
        board1.movePiece(sRow,sCol,eRow,eCol)

#board.movePiece()

#move = input("Enter move: ")
#example moves; pe4, Nf3, Nc3, be6, 
#work on move translator

#HOW MOVES WORK
#PLAYER SAYS "PIECE""POSITION"
#example: bf4
#we are looking at the bishop piece and the move f4
#first check if white has any bishop
#next check the moves of whites bishops to see it any can move to f4
#if the above are true, then we make the move, otherwise we throw an error


#Also deal with special case where two of the same piece can go to the same place
#and also case where 3 can
#and 4 can

#EX: player has a knight on c3 and g3 both can move to e4
#so if the player says, Nd5, we should check to see if we get 2 moves back
#and then return an error saying please specify which knight

#BUT we now need to handle the proper notation to make this move
#If knights are on the same row, move starts with column letter 
#if knights are on same column, move starts with row number

#Actually lets just not let the player move
#set up logic for rest of pieces
#and then just focus on making sure the bot makes one right move





#Go through every piece that white has, put them all into this moves list
#translate the moves list to chess notation
#check if the move the user entered exists in the list, if so make the move, if not say invalid
#moves = board.getPiece(pieceRow,pieceCol).moves(board.board)

#BETTER WAY TO DO COORDINATE SYSTEM WHERE MOVES ARE SEEN 





