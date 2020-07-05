con = [int(n) for n in input().split( )]
le,m = con[0],con[1]
ret = []
for i in range(le):
    ret.append(i+1)
while m:
    cmd = [int(n) for n in input().split( )]
    l,r = cmd[0], cmd[1]
    temp = ret[l-1:r]
    temp.reverse()
    ret = ret[:l-1] + temp + ret[r:]
    m -= 1
for j in ret:
    print(j,end=" ")
    