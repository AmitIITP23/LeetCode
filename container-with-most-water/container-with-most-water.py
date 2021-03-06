class Solution:
    def maxArea(self, height: List[int]) -> int:
        start=0
        end=len(height)-1
        area=0
        while(start<end):
            area=max(area,min(height[start],height[end])*(end-start))
            if(height[start]<height[end]):
                start+=1
            else:
                end=end-1
        return area
        