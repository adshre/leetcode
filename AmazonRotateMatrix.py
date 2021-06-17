class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        """
        Do not return anything, modify matrix in-place instead.
        """
        self.transpose(n,matrix)
        self.reflect(n,matrix)
        
    def transpose(self, n, matrix):
        for i in range(n):
            for j in range(i,n):
                matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i]
    def reflect(self, n, matrix):
        for i in range(n):
            for j in range(n//2):
                matrix[i][j], matrix[i][-j-1] = matrix[i][-j-1], matrix[i][j]
                
                
                OR
                
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix[0])
        
        for i in range(n//2 + n%2):
            for j in range(n//2):
                temp = matrix[n-1-j][i]
                matrix[n-1-j][i] = matrix[n-1-i][n-1-j]
                matrix[n-1-i][n-1-j] = matrix[j][n-1-i]
                matrix[j][n-1-i] = matrix[i][j]
                matrix[i][j] = temp
        
Explaination in notebook.
