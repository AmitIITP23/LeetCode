class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left=[]
        right=[0]*len(nums)
        
        prod=1
        for i in range(len(nums)):
            left.append(prod)
            prod=prod*nums[i]
        prod=1
        for j in range(len(nums)-1,-1,-1):
            right[j]=prod
            prod=prod*nums[j]
            
        answer=[]
        for i in range(len(nums)):
            answer.append(left[i]*right[i])
        return answer
            
            
        
        