n=int(input())
for i in range(n):
    l1 = list(input())
    l2 = list(input())
    ans=sorted(list(set(l1)^set(l2)))
    print(''.join(ans),end='\n\n')