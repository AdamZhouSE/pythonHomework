num=int(input())
l=list(map(int,input().split()))
maxlength=1
result=1
s=set(l[0:1])
for i in range(len(l)-1):
    length0=len(s)
    s.add(l[i+1])
    length1=len(s)
    if length0!=length1:
        result+=1
    else:
        result-=1
    maxlength=max(maxlength,result)
print(maxlength)