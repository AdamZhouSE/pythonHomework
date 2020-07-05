s=input()
k=int(input())
if k>1:
    print(''.join(sorted(s)))
else:
    l=[]
    for i in range(len(s)):
        l.append(s[i:]+s[:i])
    print(min(l))