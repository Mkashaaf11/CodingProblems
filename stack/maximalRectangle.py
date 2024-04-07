class Solution:
 
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        col = len(matrix[0])
        row = len(matrix)
        v = [int(x) for x in matrix[0]]
        maximum = self.MAH(v)
        if row > 1:
            for i in range(1,row):
                for j in range(col):

                    if matrix[i][j]=='0':
                        v[j]=0
                    else:
                        v[j]+=int(matrix[i][j])
                maximum = max(maximum,self.MAH(v))
        return maximum                


    def MAH(self,arr): 
        left = []
        right = []
        stack = []
        n = len(arr)
        area=[0]*len(arr)
        width=[0]*len(arr)
        
        for i in range(n):
            while len(stack)>0 and arr[stack[-1]]>=arr[i]:
                stack.pop()
            if len(stack) == 0:
                left.append(-1) 
            else:
                left.append(stack[-1])
            stack.append(i)

        stack.clear()
        for i in range(n-1,-1,-1): 
            while len(stack)>0 and arr[stack[-1]]>=arr[i]:
                stack.pop()
            if len(stack) == 0:
                right.append(n) 
            else:
                right.append(stack[-1])
            stack.append(i) 
        right.reverse()

        for i in range(n):
            width[i]=right[i]-left[i]-1
            area[i]=arr[i]*width[i]
        
        return max(area)


        