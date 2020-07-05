def re(n):
    if n==1:
        return 1
    else:
        return re(n-1)+n

N=int(input())
s=[]
out=[]
for i in range(N):
    s.append(input().split(' '))
for i in s:
    if int(i[0])<=int(i[1]):
        out.append(0)
        continue
    else:
        if (int(i[0])-int(i[1]))>=re(int(i[1])):
            out.append(1)
for i in out:
    print(i)

    