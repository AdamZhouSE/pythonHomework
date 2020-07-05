a=int(input().strip())
for i in range(a):
    line=input().strip()
    index=int(line.split()[2])
    s=[int(x) for x in input().strip().split()]
    t=[int(x) for x in input().strip().split()]
    m=s+t
    m.sort()
    print(m[index-1])