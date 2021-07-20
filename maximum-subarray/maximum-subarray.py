class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans=nums[0]
        m=nums[0]
        if(len(nums)==1):
            return nums[0]
        for i in range(1,len(nums)):
            if(ans<0):
                ans=0
            ans=ans+nums[i]
            
            
            m=max(ans,m)
            
        return m