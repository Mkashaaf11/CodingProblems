class Solution:
    # Back-end complete function Template for Python 3
    
    # Function to find the leaders in the array.
    def leaders(self, n, arr):
        maximum = arr[n-1]
        ans = []
        ans.append(maximum)
        
        for i in range(n-2, -1, -1):
            if arr[i] >= maximum:
                maximum = arr[i]
                ans.append(maximum)
        
        # Return the reversed list to maintain the correct order of leaders
        return list(reversed(ans))
