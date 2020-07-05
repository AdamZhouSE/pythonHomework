def is_equal(p1,p2):
    if p1[0]==p2[0] or p1[1]==p2[1]:
        return True
    return False

n=int(input())
pos=[]
for _ in range(n):
    p=list(map(int,input().split()))
    pos.append(p)
res=0
for i in range(n-1):
    for j in range(i+1,n):
        if is_equal(pos[i],pos[j]):res+=1

print(res)