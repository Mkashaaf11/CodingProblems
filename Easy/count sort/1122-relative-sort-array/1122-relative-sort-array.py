class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        countArray = [0]*10001
        result = []
        for i in arr1:
            countArray[i]+=1

        for i in arr2:
            length = countArray[i]
            for j in range(length):
                result.append(i)
                countArray[i]-=1
        for i in range(10001):
            if countArray[i]>0:
                length = countArray[i]
                for j in range(length):
                   result.append(i)
                   countArray[i]-=1
        return result

