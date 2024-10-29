class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row = len(matrix)
        col = len(matrix[0])

        rowarr= [0]*row
        colarr = [0]*col

        for i in range(row):
            for j in range(col):
                if matrix[i][j] == 0:
                    rowarr[i] = 1
                    colarr[j] = 1

        for i in range(row):
            for j in range(col):
                if rowarr[i]:
                    matrix[i][j] = 0
                if colarr[j]:
                    matrix[i][j] = 0
        return matrix                

        