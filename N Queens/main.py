class Board:

    def __init__(self , size):
        self.size = size
        self.board = create_empty_board(size)

    def __str__(self):
        out = ""
        for i in range(0,self.size):
            for j in range(0,self.size):
                cell = self.board[i][j]
                out+= f"({cell.x},{cell.y})"
                # out += ' ☐ '
            out += "\n"
    
        return out

class Cell:
    def __init__(self, x,y):
        self.x = x
        self.y = y
        self.filled = False
        self.checked = False

    def __str__(self):
        return f"({self.x},{self.y})"

    def get_neighbours(self, board : Board):
        neighbours = []
        for i in range(self.x-1 , self.x+2):
            for j in range(self.y-1, self.y+2):
                if(i>=0 and j >=0 and i<board.size and j<board.size and (not(i==self.x and j == self.y))):
                    neighbours.append(board.board[i][j])

        return neighbours

    def get_X_pattern_cells(self,board):
        cells = []
        i = self.x
        j = self.y
        while i>=0 and j>=0:
            if not(i == self.x and j == self.y):
                cells.append(board.board[i][j])
            i-=1
            j-=1
        
        i = self.x
        j = self.y
        while i>=0 and j<board.size:
            if not(i == self.x and j == self.y):
                print( f"{i},{j}\n")
                cells.append(board.board[i][j])
            i-=1
            j+=1

        i = self.x
        j = self.y
        while i < board.size and j>=0:
            if not(i == self.x and j == self.y):
                cells.append(board.board[i][j])
            i+=1
            j-=1

        i = self.x
        j = self.y
        while i<board.size and j<board.size:
            if not(i == self.x and j == self.y):
                cells.append(board.board[i][j])
            i+=1
            j+=1

        return cells
        
    def get_plus_pattern_cells(self, board):
        pass
    


def create_empty_board(size:int):
    board = [[Cell(i,j) for i in range(size)] for j in range(size)]
    
    return board

def main():
    board = Board(8)

    print(board)
    print("\u2655")
    for cell in board.board[5][5].get_X_pattern_cells(board):
        print(cell)


main()
