class Piece:
    def __init__(self, colour: int, row :int, col:int):
        self.colour = colour # 1 for white, -1 for black
        self.symbol = ""
        self.hasMoved = False
        self.row = row
        self.col = col
    
    

class Pawn(Piece):
    def __init__(self, colour: str, row: int ,col: int):
        super().__init__(colour,row,col)
        self.symbol = "P"
        self.firstmove = False
        self.potentialenPassant = False
        
        
    def __repr__(self):
        return self.symbol.upper() if self.colour == 1 else self.symbol.lower()
        
    def safeAccess(self, board, row, col):
        try:
            return board[row][col]
        except IndexError:
            return None
        
    #determine what square the pawn can move too and return as a list
    def moves(self, board):
        moves = []
        
        #All moves no filter
        if self.firstmove:
            forwardMove = [
                [self.row + (1 * self.colour), self.col],
                [self.row + 2 * self.colour ,self.col]
            ]
        else:
            forwardMove = [[self.row + (1 * self.colour), self.col]]
            
        captureMove = [
            [self.row + self.colour, self.col + 1],
            [self.row + self.colour, self.col - 1]
        ]
        
        enPassant = [
            [self.row,self.col + 1],
            [self.row,self.col - 1]
        ]
        
        
        
        
        #VALIDATE MOVES 
        validForward = []
        
        for move in forwardMove:
            row,col = move
            if row == 8 or row == -1:
                break;
            if board[row][col] != None:
                break;
            else:
                validForward.append(move)
        
        
        
        validCaptures = []
        for capture in captureMove:
            row,col = capture
            piece = self.safeAccess(board, row, col)
            if piece is None:
                continue
            if piece.colour != self.colour:
                validCaptures.append(capture)
        
        
        validEnpassant=[]
        
        for capture in enPassant:
            row,col = capture
            piece = self.safeAccess(board, row, col)
            if piece is None:
                continue
            if piece.colour != self.colour and piece.potentialenPassant == True:
                validEnpassant.append(capture)
        
        moves.extend(validForward)
        moves.extend(validCaptures)
        moves.extend(validEnpassant)
        #can this so the for loops append directly to moves but fine for now
        print(moves)
        
        
    
