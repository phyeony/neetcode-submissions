class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        col = set()
        row = set()
        square = set()
        boardLen = len(board)
        for i in range(boardLen):
            row = set()
            col = set()
            for j in range(boardLen):
                # row first
                element = board[i][j]
                if element == '.':
                    continue;  
        
                if element in row:
                    return False
                row.add(element)

        for i in range(boardLen):
            col = set()
            for j in range(boardLen):        
                # column next
                element = board[j][i]
                if element == '.':
                        continue;  
                if element in col:
                    return False
                col.add(element)

        for sqIdx in range(boardLen):
            square = set()
            for i in range(3):
                for j in range(3):
                    row = sqIdx // 3 * 3 + i
                    col = sqIdx % 3 * 3 + j
                    element = board[row][col] 
                    if element == '.':
                        continue;  
            
                    if element in square:
                        return False
                    square.add(element)
        return True
          
