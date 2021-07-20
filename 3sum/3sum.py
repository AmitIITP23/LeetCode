class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        a=[]
        nums.sort()
        for i in range(len(nums)):
            Y=0-nums[i]
            j=i+1
            k=len(nums)-1
            while(j<k):
                if (nums[j]+nums[k]==Y):
                    a.append([nums[i],nums[j],nums[k]])
                    j=j+1
                    k=k-1
                elif(nums[j]+nums[k]<Y):
                    j+=1
                elif(nums[j]+nums[k]>Y):
                    k-=1
        b=[]
        for i in a:
            if i not in b:
                b.append(i)
        return b
        