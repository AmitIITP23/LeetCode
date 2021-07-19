# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        n1=0
        m=1
        a=l1
        while(a!=None):
            n1=n1+m*a.val
            a=a.next
            m=m*10
        m=1
        b=l2
        n2=0
        while(b!=None):
            n2=n2+m*b.val
            b=b.next
            m=m*10
        ans=n1+n2
        x=None
        if(ans==0):
            t2=ListNode(0,None)
            return t2
        while(ans>0):
            temp=ListNode(ans%10,x)
            ans=ans//10
            x=temp
        prev=None
        n=None
        while(x!=None):
            n=x.next
            x.next=prev
            prev=x
            x=n
            
            
            
        return prev
        
    
        
        