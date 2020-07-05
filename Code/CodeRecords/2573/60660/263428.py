l=[2,2,4,8,16,512,256,134217728,65536]
n=int(input())
for i in range(n):
    k=int(input())
    if k<=len(l):
        print(l[k-1])
    else:
        print(k)