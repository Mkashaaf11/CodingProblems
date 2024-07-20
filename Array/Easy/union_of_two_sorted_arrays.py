class Solution:
    
    #Function to return a list containing the union of the two arrays.
    def findUnion(self,arr1,arr2,n,m):
        '''
        :param a: given sorted array a
        :param n: size of sorted array a
        :param b: given sorted array b
        :param m: size of sorted array b
        :return:  The union of both arrays as a list
        '''
        # code here 
        i=0
        j=0
        seen = set()
        unionarr=[]
        
        while i<n and j<m:
            if arr1[i]<arr2[j]:
                if arr1[i] not in seen:
                    unionarr.append(arr1[i])
                    seen.add(arr1[i])
                i+=1
            elif arr1[i] == arr2[j]:
                if arr1[i] not in seen:
                    unionarr.append(arr1[i])
                    seen.add(arr1[i])
                i+=1
                j+=1
            
            else:
                if arr2[j] not in seen:
                    unionarr.append(arr2[j])
                    seen.add(arr2[j])
                j+=1
                
        while i<n:
            if arr1[i] not in seen:
                unionarr.append(arr1[i])
                seen.add(arr1[i])
            i+=1
            
        while j<m:
            if arr2[j] not in seen:
                unionarr.append(arr2[j])
                seen.add(arr2[j])
            j+=1         
        
        return unionarr