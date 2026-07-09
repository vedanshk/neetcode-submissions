class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        m, n = len(matrix) , len(matrix[0])
        # tranpose matrix
        for i in range(m):
            for j in range(n):
                if i < j:
                    tmp = matrix[i][j]
                    matrix[i][j] =  matrix[j][i]
                    matrix[j][i] =  tmp
        
        # reverse each row
        for i in range(m):
            matrix[i].reverse()