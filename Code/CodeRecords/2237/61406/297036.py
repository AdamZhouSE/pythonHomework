nm = input().split(' ')
n = int(nm[0])
m = int(nm[1])
source = []
source1 = []
for a in range(1,n+1):
    source.append(a)
for a in range(0,m):
    opt = input().split(' ')
    start = int(opt[0])
    end = int(opt[1])
    source1 = source[start-1:end]
    source1.reverse()
    source = source[:start-1]+source1+source[end:]
for i in source:
    print(i,end=' ')