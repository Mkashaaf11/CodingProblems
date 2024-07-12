class Solution:
    def armstrongNumber (self, n):
        # code here 
        num = n
        sum = 0
        
        while num>0:
            cube = pow(num%10,3)
            sum = sum + cube
            num = num//10
        
        return 'true' if sum == n else 'false'
