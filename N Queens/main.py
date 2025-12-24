class Colors:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    ENDC = '\033[0m' # Resets the color/style

class Board:

    def __init__(self , size):
        self.size = size
        self.board = create_empty_board(size)
        self.clean_cells = []
        self.queen_positions = []
        self.cells = self.get_all_cells()
        self.clean_cells = self.cells
        
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

                if(cell.dirty):
                    out += Colors.RED + ' ☐ ' + Colors.ENDC
                elif(cell.has_queen):
                    out += " \u2655 "
                else:
                    out += Colors.GREEN + ' ☐ ' + Colors.ENDC

            out += "\n"
    
        return out
    
    def find_clean_cells(self):
        dirty_cells = []
        for pos in self.queen_positions:
            for cell in self.board[pos[0]][pos[1]].get_box_pattern_cells(self):
                dirty_cells.append(cell)
                cell.dirty = True
            for cell in self.board[pos[0]][pos[1]].get_X_pattern_cells(self):
                dirty_cells.append(cell)
                cell.dirty = True
            for cell in self.board[pos[0]][pos[1]].get_plus_pattern_cells(self):
                dirty_cells.append(cell)
                cell.dirty = True
            dirty_cells.append(pos)
            # self.board[pos[0]][pos[1]].dirty = True
            self.board[pos[0]][pos[1]].has_queen = True
            

        return list(set(self.clean_cells) - set(dirty_cells))


class Cell:
    def __init__(self, x,y):
        self.x = x
        self.y = y
        self.dirty = False
        self.has_queen = False

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
    



def create_empty_board(size:int):
    board = [[Cell(i,j) for i in range(size)] for j in range(size)]
    
    return board

def main():
    board = Board(8)
    print(board)

    x = int(input("Enter Queen X PoS: "))
    y = int(input("Enter Queen Y PoS: "))

    board.queen_positions.append((x,y))
    board.find_clean_cells()

    print(board)


main()
