s=input()
k=int(input())
start,end,res=0,0,0
charNum=[0,0]
charNum[0]+=1
while len(s)>end:
    maxChar=max(charNum)
    if maxChar+k>end-start:
        end+=1
        if end<len(s):
            if s[end]==s[0]:
                charNum[0]+=1
            else:
                charNum[1]+=1
    else:
        if s[start]==s[0]:
            charNum[0]-=1
        else:
            charNum[1]-=1
        start+=1
    if maxChar+k>res:
        if maxChar+k<=len(s):
            res=maxChar+k
        else:
            res=len(s)
print(res)