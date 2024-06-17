class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        for i in range(c+1):
            for j in range(i,c+1):
                if (i*i)+(j*j) == c:
                    return True
        return False