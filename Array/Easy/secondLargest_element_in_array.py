class Solution:
    def print2largest(self, arr):
        largest = -1
        secondLargest = -1
        for i in range(len(arr)):
            if arr[i] > largest:
                secondLargest = largest
                largest = arr[i]
            elif arr[i] > secondLargest and arr[i] != largest:
                secondLargest = arr[i]
        
        return secondLargest