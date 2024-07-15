from typing import List


class Solution:
    def largest(self, n : int, arr : List[int]) -> int:
        # code here
        max = arr[0]
        for i in range(1,n):
            if arr[i]>max:
                max=arr[i]
        return max        
        