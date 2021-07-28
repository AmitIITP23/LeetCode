class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        i=0
        j=0
        a=[]
        while(i<len(nums1) and j<len(nums2)):
            if(nums1[i]<nums2[j]):
                a.append(nums1[i])
                i+=1
            else:
                a.append(nums2[j])
                j+=1
        if(i==len(nums1)):
            a=a+nums2[j:]
        else:
            a=a+nums1[i:]
        if(len(a)%2==1):
            x=0
            y=len(a)-1
            mid=(x+y)//2
            return a[mid]/1.0
        else:
            x=0
            y=len(a)-1
            mid=(x+y)//2
            return (a[mid]+a[mid+1])/2.0
            
        
        