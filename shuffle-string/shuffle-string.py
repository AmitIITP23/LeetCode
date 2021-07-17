class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        a=[0]*len(s)
        st=""
        for i in range(len(s)):
            a[indices[i]]=s[i]
        for i in a:
            st=st+i
        return st
            
        
        