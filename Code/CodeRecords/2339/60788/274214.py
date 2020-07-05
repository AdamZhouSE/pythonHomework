a=int(input().strip())
for i in range(a):
    length=int(input().strip())
    t=[x for x in input().strip().split()]
    count=0
    for p in range(len(t)-1):
        for q in range(p+1,len(t)):
            if t[p]>t[q]:
                count+=1
    print(count)
            