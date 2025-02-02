class Piece:
    def __init__(self, colour: int, row :int, col:int, board):
        self.colour = colour # 1 for white, -1 for black
        self.symbol = ""
        self.hasMoved = False
        self.row = row
        self.col = col
        self.board = board
        
        if colour == 1:
            board.whitePieces.append(self)
        else:
            board.blackPieces.append(self)
    
    def safeAccess(self, row, col): #Remove out of bounds moves
        try:
            return self.board.board[row][col]
        except IndexError:
            return None
            
    def moves(self):
        moves = []
        possibleMoves = self.capturables()
        for move in possibleMoves:
            row, col = move
            if self.safeAccess(row, col) is None:
                moves.append(move)
            elif self.safeAccess(row, col).colour != self.colour:
                moves.append(move)
        return moves
    
    def __repr__(self):
        return self.symbol.upper() if self.colour == 1 else self.symbol.lower()
    

class Pawn(Piece):
    def __init__(self, colour: int, row: int ,col: int, board):
        super().__init__(colour,row,col,board)
        self.symbol = "P"
        self.firstmove = True
        self.potentialenPassant = False
        
        #used to make sure king is not walking through checks
    def capturables(self): #Returns a theoretical squares a pawn could capture
        possibleCaptures = [
            [self.row + self.colour, self.col + 1],
            [self.row + self.colour, self.col - 1]
        ]
        
        validCaptures = [
            [r, c]
            for r, c in possibleCaptures
                if 0 <= r < 8 and 0 <= c < 8
        ]
        return validCaptures
            
    def normalCaptures(self): #Returns actual squares a pawn could capture
        captures = [
            [self.row + self.colour, self.col + 1],
            [self.row + self.colour, self.col - 1]
        ]
        
        validCaptures = []
        for capture in captures:
            row,col = capture
            piece = self.safeAccess(row, col)
            if piece is None:
                continue
            if piece.colour != self.colour:
                validCaptures.append(capture)
        return validCaptures
        
    def enPassantCaptures(self): #Returns actual squares a pawn could capture
        enPassant = [
            [self.row,self.col + 1],
            [self.row,self.col - 1]
        ]
        
        validEnpassant=[]
        
        for capture in enPassant:
            row,col = capture
            piece = self.safeAccess(row, col)
            if piece is None:
                continue
            if piece.colour != self.colour and piece.potentialenPassant == True:
                validEnpassant.append(capture)
        return validEnpassant
    
    def forwardMoves(self):
        if self.firstmove:
            forwardMove = [
                [self.row + (1 * self.colour), self.col],
                [self.row + 2 * self.colour ,self.col]
            ]
        else:
            forwardMove = [[self.row + (1 * self.colour), self.col]]
            
        validForward = []
        
        for move in forwardMove:
            row,col = move
            if row == 8 or row == -1:
                break;
            if self.board.board[row][col] != None:
                break;
            else:
                validForward.append(move)
        return validForward
    
    #determine what square the pawn can move too and return as a list
    #make this return possible moves
    def pawnMoves(self):
        moves = []
        
        validForward = self.forwardMoves()
        validCaptures = self.normalCaptures()
        validEnpassant = self.enPassantCaptures()
        
        
        
        
        moves.extend(validForward)
        moves.extend(validCaptures)
        moves.extend(validEnpassant)
        return moves
        
class King(Piece):
    def __init__(self, colour: str, row: int ,col: int, board):
        super().__init__(colour,row,col,board)
        self.symbol = "K"
        self.inCheck = False
        self.firstMove = True
        self.castleKingside = False
        self.castleQueenside = False 
        # keep track of this through game manager
        
        
    def moves(self):
        possibleMoves = []
        current_row = self.row
        current_col = self.col

        # Generate all adjacent king moves (including current position)
        for dr in [-1, 0, 1]:
            for dc in [-1, 0, 1]:
                # Skip the current position (no move)
                if dr == 0 and dc == 0:
                    continue
                
                new_row = current_row + dr
                new_col = current_col + dc
                
                # Check if move is within board boundaries (0-7 for 8x8 board)
                if 0 <= new_row < 8 and 0 <= new_col < 8:
                    possibleMoves.append([new_row, new_col])
        #Right now moves are all the theoretical ways a king could move on an empty board
        
        #ADD CASTLING
        
        validMoves = []
        for move in possibleMoves:
            row,col = move
            piece = self.safeAccess(row, col)
            if piece is None:
                validMoves.append(move)
            elif piece.colour != self.colour:
                validMoves.append(move)
        
        
        enemyCapturables = self.board.getAllEnemyCapturableSquare(self.colour)
        #add check to make sure enemycapturables isnt empty or NoneType
        enemyCapturables = [i for sublist in enemyCapturables for i in sublist]
        
        
        moves = []
        #moves = [x for x in validMoves if x not in enemyCapturables]
        moves = [move for move in validMoves if move not in enemyCapturables]
        
        #moves = [x for x in validMoves if x not in enemyCapturables]
        
        return moves

class Knight(Piece):
    def __init__(self, colour: int, row: int ,col: int, board):
        super().__init__(colour,row,col,board)
        self.symbol = "N"
        self.firstmove = True
    
    def capturables(self):
        possibleCapturables = []
        current_row = self.row
        current_col = self.col
        knight_moves = [
            (-2, -1), (-2, 1), (2, -1), (2, 1),  # Moves with 2-row jump
            (-1, -2), (-1, 2), (1, -2), (1, 2)   # Moves with 2-column jump
        ]

        for dr, dc in knight_moves:
            new_row = current_row + dr
            new_col = current_col + dc

            # Check if the move stays within board limits
            if 0 <= new_row < 8 and 0 <= new_col < 8:
                possibleCapturables.append([new_row, new_col])

        return possibleCapturables # returns moves in bounds
    
        
class Rook(Piece):
    def __init__(self, colour: int, row: int ,col: int, board):
        super().__init__(colour,row,col,board)
        self.symbol = "R"
        self.firstmove = True
        
        
        
    def capturables(self):
        row, col = self.row, self.col
        capturables = []
        
        # Directions for the rook: (row change, col change)
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # Right, Left, Down, Up
        
        for dr, dc in directions:
            currentRow, currentCol = row, col
            while True:
                currentRow += dr
                currentCol += dc
                
                # Check boundaries
                if currentRow < 0 or currentRow > 7 or currentCol < 0 or currentCol > 7:
                    break  # Stop if out of bounds
                
                square = self.safeAccess(currentRow, currentCol)
                
                if square is None:  # Empty square, add to capturables
                    capturables.append([currentRow, currentCol])
                else:  # Found a piece, capture and stop
                    capturables.append([currentRow, currentCol])
                    break  # Stop in this direction
            
        return capturables
        
        
        
class Bishop(Piece):
    def __init__(self, colour: int, row: int ,col: int, board):
        super().__init__(colour,row,col,board)
        self.symbol = "B"
        self.firstmove = True
        
    def capturables(self):
        row, col = self.row, self.col
        capturables = []
        directions = [(1, 1), (-1, 1), (-1, -1), (1, -1)]  # Right, Left, Down, Up
        
        for dr, dc in directions:
            currentRow, currentCol = row, col
            while True:
                currentRow += dr
                currentCol += dc
                
                # Check boundaries
                if currentRow < 0 or currentRow > 7 or currentCol < 0 or currentCol > 7:
                    break  # Stop if out of bounds
                
                square = self.safeAccess(currentRow, currentCol)
                
                if square is None:  # Empty square, add to capturables
                    capturables.append([currentRow, currentCol])
                else:  # Found a piece, capture and stop
                    capturables.append([currentRow, currentCol])
                    break  # Stop in this direction
        return capturables
                    
    
        
class Queen(Piece):
    def __init__(self, colour: int, row: int ,col: int, board):
        super().__init__(colour,row,col,board)
        self.symbol = "Q"
        self.firstmove = True
        
    def capturables(self):
        row, col = self.row, self.col
        capturables = []
        directions = [(1, 1), (-1, 1), (-1, -1), (1, -1)]  # Right, Left, Down, Up
        
        for dr, dc in directions:
            currentRow, currentCol = row, col
            while True:
                currentRow += dr
                currentCol += dc
                
                # Check boundaries
                if currentRow < 0 or currentRow > 7 or currentCol < 0 or currentCol > 7:
                    break  # Stop if out of bounds
                
                square = self.safeAccess(currentRow, currentCol)
                
                if square is None:  # Empty square, add to capturables
                    capturables.append([currentRow, currentCol])
                else:  # Found a piece, capture and stop
                    capturables.append([currentRow, currentCol])
                    break  # Stop in this direction
        
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # Right, Left, Down, Up
        
        for dr, dc in directions:
            currentRow, currentCol = row, col
            while True:
                currentRow += dr
                currentCol += dc
                
                # Check boundaries
                if currentRow < 0 or currentRow > 7 or currentCol < 0 or currentCol > 7:
                    break  # Stop if out of bounds
                
                square = self.safeAccess(currentRow, currentCol)
                
                if square is None:  # Empty square, add to capturables
                    capturables.append([currentRow, currentCol])
                else:  # Found a piece, capture and stop
                    capturables.append([currentRow, currentCol])
                    break  # Stop in this direction
                     
        return capturables
                    