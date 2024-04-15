class Solution:
    
    #Function to find maximum of each subarray of size k.
    def max_of_subarrays(self,arr,n,k):
        
        i=0
        j=0
        mx = -1
        maxarr = []
        while j<n:
            if arr[j]>=mx:
                mx=arr[j]
            if j-i+1<k:
                j+=1
            elif j-i+1==k:
                maxarr.append(mx)
                if k==1:
                    mx=float('-inf')
                elif arr[i]==mx:
                    mx=max(arr[i+1:j+1])
                i+=1
                j+=1
                
        return maxarr   