class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        n = len(matrix)         # row length
        m = len(matrix[0])      # column length
        
        left = 0
        right = m - 1
        up = 0
        down = n - 1
        
        ans = []
        
        while len(ans) < n * m:
            
            # move left to right
            for i in range(left, right + 1):        # + 1 so that right equals m
                ans.append(matrix[up][i])           # ex : row[0] and columns[i]
            
            # move up to down 
            for i in range(up + 1, down + 1) :
                ans.append(matrix[i][right])       # ex : row[i] and column[m]
                
            # move right to left
            if up < down :                         # avoid duplicates
                for i in range(right - 1, left - 1 , -1) : # left - 1 to get left = 0
                    ans.append(matrix[down][i])
            
            # move down to up
            if left < right :
                for i in range(down - 1, up, -1):
                    ans.append(matrix[i][left])
        
            left += 1
            right -= 1
            up += 1
            down -= 1
        return ans
            
                
        
