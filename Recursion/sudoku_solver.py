'''
Sudoku Solver :- solve a Sudoku puzzle by filling the empty cells.
'''

class Solution:
    def check(self,sudoku,i,j,k):
        for x in range(9):
            if sudoku[i][x] == k:
                return False
            if sudoku[x][j] == k:
                return False
            
            if sudoku[3*(i//3)+x//3][3*(j//3)+x%3] == k:
                return False 
            
        return True
    
    
    def solve(self,sudoku):
        for i in range(len(sudoku)):
            for j in range(len(sudoku)):
                if sudoku[i][j] == '.':
                    for k in range(1,10):
                        if self.check(sudoku,i,j,str(k)):
                            sudoku[i][j] = str(k)
                            if self.solve(sudoku) == True:
                                return True
                            else:
                                sudoku[i][j] = '.'
                    return False
        return True
                    
    def solveSudoku(self, board: List[List[str]]) -> None:
        self.solve(board)
        

T.C. :- O(9^(n*n))
S.C. :- (n*n)