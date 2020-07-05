s=list(input())
k=int(input())
if k>=2:
    s.sort()
    print(''.join(i for i in s))
elif k==1:
    ind=s.index(min(s))
    for i in range(ind,len(s)):
        print(s[i],end="")
    for i in range(0,ind):
        print(s[i],end="")
    print()
else:
    print(''.join(i for i in s))