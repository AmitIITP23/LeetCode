class Solution:
    def sortSentence(self, s: str) -> str:
        i=0
        t=''
        a=[]
        while(i<len(s)):
            if(s[i]==' '):
                a.append(t)
                t=''
            else:
                t=t+s[i]
            i=i+1
        a.append(t)
        x=0
        for i in a:
            if int(i[len(i)-1])>x:
                x=int(i[len(i)-1])
        h=[None]*x
        for i in a:
            h[int(i[len(i)-1])-1]=i[:len(i)-1]
        p=''
        for i in h:
            p=p+i+' '
        return p[:len(p)-1]
            
            
            
            
            
                

        