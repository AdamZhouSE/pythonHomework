num=int(input().strip())
for i in range(num):
    line1=input().strip()
    s=[int(x) for x in input().strip().split()]
    t=[int(x) for x in input().strip().split()]
    s+=t
    s.sort()
    print(' '.join([str(x) for x in s]),end=' ')
    print("")
    
    