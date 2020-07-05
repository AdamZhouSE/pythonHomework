def func(lines,x,y):
    s=lines[x-1]
    t=lines[y-1]
    len1=len(s)
    len2=len(t)
    cnt=0
    for i in range(len2-len1+1):
        found=True
        for j in range(len1):
            if s[j]!=t[j+i]:
                found=False
                break
        if found: cnt+=1
    return cnt
str=input()
lines=[]
tmp=""
for ch in str:
    if ch=='P': lines.append(tmp)
    elif ch=='B': tmp=tmp[:-1]
    else: tmp+=ch
t=int(input())
for i in range(t):
    nums=[int(x) for x in input().split()]
    print(func(lines,nums[0],nums[1]))