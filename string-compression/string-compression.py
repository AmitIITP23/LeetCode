class Solution:
    def compress(self, chars: List[str]) -> int:
        index=0
        ans=0
        count=1
        l=len(chars)
        if(l==1):
            return 1
        else:
            
            for i in range(l-1):
                if(chars[i]==chars[i+1]):
                    count=count+1
                else:
                    chars[index]=chars[i]
                    ans=ans+1
                    index=index+1
                    if(count>1 and count<10):
                        chars[index]=str(count)
                        ans+=1
                        index+=1
                    elif(count>9):
                        t=[]
                        temp=count
                        while(temp>0):
                            t.append(temp%10)
                            temp=temp//10
                        t=t[::-1]
                        for i in range(len(t)):
                            chars[index]=str(t[i])
                            ans+=1
                            index+=1
                    count=1
        chars[index]=chars[i+1]
        index=index+1
        ans=ans+1
        if(count>1 and count<10):
            chars[index]=str(count)
            ans+=1
            index+=1
        elif(count>9):
            t=[]
            temp=count
            while(temp>0):
                t.append(temp%10)
                temp=temp//10
            t=t[::-1]
            for i in range(len(t)):
                chars[index]=str(t[i])
                ans+=1
                index+=1
                
        return ans
                            
                        
        