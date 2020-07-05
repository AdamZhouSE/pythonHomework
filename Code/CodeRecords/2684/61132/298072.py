def substr(l,prefix):
    if len(l)<=1:return [prefix]
    return substr(l[2:],prefix+[l[1]])+substr(l[1:],prefix+[l[0]])

def mintime(l):
    return min(map(sum,substr(l,[])))

t = int(input())
for j in range(t):
    n=int(input())
    l=list(map(int,input().split()))
    print(mintime(l))