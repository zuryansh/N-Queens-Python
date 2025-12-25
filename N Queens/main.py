import random

class Colors:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    ENDC = '\033[0m' # Resets the color/style

class Board:

    def __init__(self , size):
        self.size = size
        self.board = create_empty_board(size,self)
        self.queen_cells: list[Cell] = [] #
        self.cells: list[Cell] = self.get_all_cells()
        self.clean_cells = self.cells
        print(self.clean_cells.__len__())
        
    def get_all_cells(self):
        cells = []
        for i in range(self.size):
            for j in range(self.size):
               cells.append(self.board[i][j]) 
        
        return cells

    def __str__(self):
        out = ""
        for i in range(0,self.size):
            for j in range(0,self.size):
                cell = self.board[i][j]
                # out+= f"({cell.x},{cell.y})"
                if(cell.has_queen):
                    out += " \u2655 "
                else:
                    if(cell.dirty):
                        out += Colors.RED + ' ☐ ' + Colors.ENDC
                    
                    else:
                        out += Colors.GREEN + ' ☐ ' + Colors.ENDC

            out += "\n"
    
        return out
    
    def update(self):
        self.clean_cells = self.find_clean_cells()

    def find_clean_cells(self):
        dirty_cells = []
        for queen_cell in self.queen_cells:
            for cell in self.board[queen_cell.x][queen_cell.y].get_box_pattern_cells(self):
                dirty_cells.append(cell)
                cell.dirty = True
            for cell in self.board[queen_cell.x][queen_cell.y].get_X_pattern_cells(self):
                dirty_cells.append(cell)
                cell.dirty = True
            for cell in self.board[queen_cell.x][queen_cell.y].get_plus_pattern_cells(self):
                dirty_cells.append(cell)
                cell.dirty = True

            dirty_cells.append(queen_cell)
            # self.board[queen_cell[1]][queen_cell[0]].has_queen = True
            
            

        return list(set(self.clean_cells) - set(dirty_cells))


class Cell:
    def __init__(self, x,y, board: Board):
        self.x = x
        self.y = y
        self.dirty = False
        self.has_queen = False
        self.parentBoard: Board = board

    def place_queen_on_cell(self):
        self.has_queen = True
        self.dirty = True
        self.parentBoard.queen_cells.append(self)
        self.parentBoard.update()

    def __str__(self):
        return f"({self.x},{self.y})"

    def get_box_pattern_cells(self, board : Board):
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
        cells = []
        for i in range(0,board.size):
            if( i == self.x ): continue
            cells.append(board.board[i][self.y])
        for j in range(0,board.size):
            if( j == self.y): continue
            cells.append(board.board[self.x][j])
        
        return cells
    

def place_queen(board:Board):
    if(board.clean_cells.__len__()==0):
        global try_again
        return
    
    cell  = random.choice(board.clean_cells)
    cell.place_queen_on_cell()
    


def create_empty_board(size:int, out: Board):
    board = [[Cell(i,j, out) for i in range(size)] for j in range(size)]
    
    return board

def main():
    n  = int(input("ENTER N: "))

    board = Board(n)
    print(board)
    # board.queen_positions.append((1,0))
    for i in range(0,n):

        # x = int(input("Enter Queen X PoS: "))
        # y = int(input("Enter Queen Y PoS: "))

        # board.queen_cells.append((x,y))
        # board.find_clean_cells()
        place_queen(board)

        print(board)
        input("Press Enter for next step")

    if(board.queen_cells.__len__()<n):
        print(Colors.RED + "FAILED TRY AGAIN" + Colors.ENDC)
    

main()