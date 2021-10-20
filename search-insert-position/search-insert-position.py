class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left=0
        right=len(nums)-1
        if(target<=nums[0]):
            return 0
        
        while(left<right):
            mid=left+(right-left)//2
            if(target>nums[mid]):
                if(target<=nums[mid+1]):
                    return mid+1
                else:
                    left=mid+1
            else:
                right=mid
        return(len(nums))
        
                    
            
            
            
            
        