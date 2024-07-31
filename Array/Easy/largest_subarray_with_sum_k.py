
class Solution:
    def lenOfLongSubarr (self, arr, n, k) : 
        #Complete the function
        hashmap  = {}
        maxlength= 0 
        cumm_sum = 0
        n = len(arr)
        for i in range(n):
            cumm_sum += arr[i]
            
            if cumm_sum == k:
                maxlength = i+1
            
            if (cumm_sum - k) in hashmap:
                maxlength = max(maxlength , i - hashmap[cumm_sum-k])
            
            if cumm_sum not in hashmap:
                hashmap[cumm_sum] = i
        
        return maxlength  