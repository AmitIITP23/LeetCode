class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        ans=0
        wealth=0
        for i in range(len(accounts)):
            for j in range(len(accounts[0])):
                ans=ans+accounts[i][j]
            if(wealth<ans):
                wealth=ans
            ans=0
        return wealth
                
            