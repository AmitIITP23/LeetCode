class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        ans=[]
        temp=first
        ans.append(first)
        for i in range(len(encoded)):
            ans.append(ans[i] ^ encoded[i] )
        return ans
            
        