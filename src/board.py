class Board:
    def __init__(self):
       self.board = [[0 for x in range(8)] for y in range(8)]
       self.setup_pieces()
    def setup_pieces(self):
        self.board[0] = ["R","N","B","Q","K","B","N","R"]
        self.board[1] = ["P"]*8
        self.board[6] = ["p"]*8
        self.board[7] = ["r","n","b","q","k","b","n","r"]
    def get_piece(self, row:int, col:int) -> str |None:
        return self.board[row][col]
        
board1 = Board()

print(board1.get_piece(0,0))

