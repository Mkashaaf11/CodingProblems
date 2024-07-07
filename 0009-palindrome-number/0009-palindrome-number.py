class Solution:
    def isPalindrome(self, x: int) -> bool:
        num = abs(x)
        flag = False
        if x<0:
            flag=True
        rev = 0
       
        while num>0:
            rev = (rev*10)+num%10
            num=num//10
        
        if flag==False and rev == x:
            return True

        return False    