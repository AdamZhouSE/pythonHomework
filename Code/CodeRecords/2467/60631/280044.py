t = int(input())
for ti in range(t):
    s=input()
    l1 = input().split(' ')
    l2 = input().split(' ')
    l = l1+l2
    out=[]
    for i in l:
        out.append(int(i))
    out=sorted(out)
    print(out[int(s[-1])-1])