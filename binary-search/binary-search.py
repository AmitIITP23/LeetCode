class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start=0
        count=0
        mid=0
        l=len(nums)
        end=len(nums)-1
        while(start<=end):
            
            
                
            mid=(start+end)//2
            if(nums[mid]==target):
                return mid
            else:
                if(nums[mid]>target):
                    end=mid-1
                else:
                    start=mid+1
            
        return -1
                    
        