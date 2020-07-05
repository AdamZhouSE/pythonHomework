n=int(input())
strs=[]
lens=[]
for i in range(n):
    s=input()
    strs.append(s)
    lens.append(len(s))
maxlen=min(lens)
s=strs[lens.index(min(lens))]
for i in range(len(s),0,-1):
    j=0
    while(j+i<=len(s)):
        ans=1
        for string in strs:
            if s[j:j+i] not in string:
                ans=0
                break
        if(ans==1):
            print(i)
            break
        j+=1
    if(ans==1):
        break
        
    