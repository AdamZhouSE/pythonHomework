k,m=map(int,input().split(" "))
src=[c for c in input()]
nums=int(input())
for i in range(nums):
    a,b,c=map(int,input().split(" "))
    temp=[src[i] for i in range(a,b)]
    idx=0
    for pos in range(c,c+b-a):
        src.insert(pos,temp[idx])
        idx+=1
    while len(src)>m:
        src.pop()
print("".join(src[0:k]),end='')