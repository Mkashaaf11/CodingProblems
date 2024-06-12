class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        count = [0] * 101
        for h in heights:
            count[h]+=1
        expected = []
        for i in range(1,101):
            value = count[i]
            for j in range(value):
                expected.append(i)

        result = 0
        for i in range(len(heights)):
            if heights[i]!=expected[i]:
                result+=1
        return result                

