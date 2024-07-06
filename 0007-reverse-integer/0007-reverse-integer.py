class Solution:
    def reverse(self, x: int) -> int:
        neg =  False
        n = abs(x)
        rev = 0

        if x<0:
            neg = True
        while n>0:
            rev = (rev * 10) + n%10
            n = n//10

        if neg == True:
            rev*= -1
            
        return rev        


        