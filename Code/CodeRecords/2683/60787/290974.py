t=int(input())
for ex in range(0,t):
    s=list(input())
    re=[]
    temp=0
    for i in range(1,len(s)):
        if s[i]>=s[i-1]:
            temp+=1
        else:
            re.append(temp)
            temp=0
    re.append(temp)
    print(max(re))