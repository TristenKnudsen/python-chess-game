class chessGame():
    def __init__(self):
        self.board = [[None for x in range(8)] for y in range(8)]
        self.whitePieces = []
        self.blackPieces = []
        
    def printBoardTesting(self):
        for row_num, c in enumerate(self.board[::-1], start=1): 
            formattedRow = [str(piece) if piece else "." for piece in c]
            print(f"{8 - row_num} {' '.join(formattedRow)}")        
        print("  0 1 2 3 4 5 6 7")     
        
    def addPiece(self,colour,piece): 
        if colour == 1:
            self.whitePieces.append(piece)
        elif colour == -1:
            self.blackPieces.append(piece)
            
        self.board[piece.row][piece.col] = piece
    def getPiece(self, row, col):
        return self.board[row][col]
        
    def getAllEnemyCapturableSquare(self, colour):
        capturable = []
        colourPieces = []
        
        if colour == 1:
            colourPieces = self.blackPieces
        else:
            colourPieces = self.whitePieces

        for piece in colourPieces:
            capturable.extend(piece.capturables())
                
        return capturable
        
class Piece():
    def __init__(self, colour, row, col):
        self.colour = colour
        self.symbol = ""
        self.row = row
        self.col = col
    
    def __repr__(self):
        return self.symbol.upper() if self.colour == 1 else self.symbol.lower()
    
    def moves():
        pass
    
    def capturables():
        pass
        
class King(Piece):
    def __init__(self, colour: str, row: int ,col: int):
        super().__init__(colour,row,col)
        self.symbol = "K"
        self.inCheck = False
        self.firstMove = True
        self.castleKingside = False
        self.castleQueenside = False 
        
    def capturables(self):
        row, col = self.row, self.col
        capturables = []
        for dr in [-1, 0, 1]:
            for dc in [-1, 0, 1]:
                if dr == 0 and dc == 0:
                    continue
                
                if 0 <= row + dr < 8 and 0 <= col + dc < 8:
                    capturables.append([row + dr, col + dc])
        return capturables
    
    def validateMoves(self, board):
        capturables = capturables(self)
        
        
        
        
        
    
game1 = chessGame()
game1.addPiece(-1,King(-1,1,1))
print(game1.getPiece(1,1).capturables())
game1.printBoardTesting()