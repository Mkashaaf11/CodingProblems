class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = len(matrix)
        cols  =len(matrix[0])
        dummy_matrix = [[0] * cols for _ in range(rows)]


        for i in range(rows):
            for j in range(cols):
                dummy_matrix[j][rows-i-1]=matrix[i][j]
        
        for i in range(rows):
            for j in range(cols):
                matrix[i][j] = dummy_matrix[i][j]  