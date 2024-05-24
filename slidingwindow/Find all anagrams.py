class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        size = len(s)
        k = len(p)
        ans = []
        #dictionary to store count of each unique character
        storeCount = {}
        for char in p:
            storeCount[char]= storeCount.get(char,0)+1    
        count = len(storeCount)
        i=0
        j=0

        while j<size:

            if s[j] in storeCount:
                storeCount[s[j]] -=1
                if storeCount[s[j]] == 0:
                    count -=1

            if j-i+1<k:       
                j+=1

            elif j-i+1 == k:
                if count == 0:
                    ans.append(i)
                if s[i] in storeCount:
                    storeCount[s[i]] += 1  
                    if storeCount[s[i]]==1:
                        count += 1  

                j+=1
                i+=1    
        return ans