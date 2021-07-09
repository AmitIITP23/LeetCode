class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        a=[]
        x=0
        for i in range(len(nums)):
            x=x+nums[i]
            a.append(x)
        return a
            