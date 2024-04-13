from collections import deque
def printFirstNegativeInteger( A, N, K):
    
    i=0
    j=0
    negnum = deque()
    ans = []
    
    while j<N:
        if A[j] < 0:
            negnum.append(A[j])
        if j-i+1 < K:
            j+=1
        elif j-i+1==K:
            if len(negnum)>0:
                ans.append(negnum[0])
                
            else:
                ans.append(0)
                
            i+=1
            j+=1
            if A[i-1]<0:
                negnum.popleft()
    return ans