class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        left = []
        right = []
        width = [0]*len(heights)
        area = [0]*len(heights)
        n = len(heights)

        #Nearest smallest left
        for i in range(n):
            if len(stack)==0:
                left.append(-1)
            elif len(stack)>0 and heights[stack[-1]]<heights[i] :
                left.append(stack[-1])
            elif len(stack)>0 and heights[stack[-1]]>= heights[i]:
                while len(stack)>0 and heights[stack[-1]]>=heights[i]:
                    stack.pop()      
                if len(stack)==0:
                    left.append(-1)
                else:
                    left.append(stack[-1])    
        
            stack.append(i)

        stack.clear()
         #Nearest smallest right
        for i in range(n-1,-1,-1):
            if len(stack)==0:
                right.append(len(heights))
            elif len(stack)>0 and heights[stack[-1]]<heights[i]:
                right.append(stack[-1])
            elif len(stack)>0 and heights[stack[-1]]>= heights[i]:
                while len(stack)>0 and heights[stack[-1]]>=heights[i]:
                    stack.pop()      
                if len(stack)==0:
                    right.append(len(heights))
                else:
                    right.append(stack[-1])    
        
            stack.append(i)
        right.reverse()
        
        for i in range(n):
            width[i]=right[i]-left[i]-1
            area[i]=width[i]*heights[i]
        
        return max(area)