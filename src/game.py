from board import Board
from pieces import Pawn, King, Knight, Rook, Bishop, Queen



class Game():
    def __init__(self):
        self.board = Board()
        self.colToIndex = { "a": 0, "b": 1, "c": 2, "d": 3, "e": 4, "f": 5, "g": 6, "h": 7 }
        self.indexToCol = self.colToIndex.__class__(map(reversed, self.colToIndex.items()))
    
    def displayBoard(self):
        if self.board.turnColour == 1:
            self.board.printBoardWhite()
        else:
            self.board.printBoardBlack()

    def promptForCoordinate(self, prompt):
        while True:
            coord = input(prompt).strip().lower()
            if len(coord) >= 2 and coord[0] in self.colToIndex and coord[1].isdigit():
                col = self.colToIndex[coord[0]]
                row = int(coord[1]) - 1
                if 0 <= row < 8:
                    return row, col
            print("Invalid coordinate. Please enter a value like e2.")

        
    def run(self):
        while True:
            turnColour = self.board.turnColour
            self.displayBoard()
            
            
            if self.board.getNumberOfMoves(turnColour) == 0:
                if self.board.colourKingInCheck(turnColour):
                    print("checkmate")
                else:
                    print("Stalemate")
                    
            
            if turnColour == 1:
                for piece in self.board.whitePieces:
                    if isinstance(piece, Pawn):
                            piece.potentialenPassant = False
            else:
                for piece in self.board.blackPieces:
                        if isinstance(piece, Pawn):
                                piece.potentialenPassant = False
            
            self.board.blackKing.checkCastleMoves(self.board) 
            sRow, sCol = self.promptForCoordinate("Enter piece coor as row col (ex. e4)")
            
            
            piece = self.board.getPiece(sRow,sCol)
            if piece is None:
                print("There is no piece on that square!")
            elif piece.colour != turnColour:
                print("Not your piece!")
            elif len(piece.moves(self.board)) == 0:
                print("This piece has no moves")
            else:
                q = 0
                print("Moves:")
                for move in piece.moves(self.board):
                    row,col = move
                    if row == "O":
                        print(str(q) + ":" + row + "-" + col)
                    else:
                        print(str(q) + ":" + str(self.indexToCol[col]) + str(int(row) + 1))
                    q += 1
                    
                while True:
                    try:
                        userMoveNumber = int(input("Select move number: "))
                        break  # Exit the loop if conversion is successful
                    except ValueError or IndexError:
                        print("Invalid input. Please enter a valid integer.")
                eRow,eCol = piece.moves(self.board)[userMoveNumber]
                
                
                self.board.movePiece(piece,eRow,eCol)
                turnColour *= -1

game = Game()
game.run()
print("Game Started")

#might change moves to work like normal chess and then use a dictionary