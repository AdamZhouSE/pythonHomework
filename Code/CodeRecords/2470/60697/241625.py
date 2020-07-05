# 2
# 3
# 1 2 3 4 5 6 7 8 9
# 2
# 56 96 91 54
t=int(input())
sizes=[]
nums=[]
for i in range(t):
    sizes.append(int(input()))
    nums.append(list(map(int,input().split(' '))))
for i in range(t):
    size=sizes[i]
    num=nums[i]
    a=size*size-size
    res=[]
    while a<size*size:
        b=a
        while b>=0:
            res.append(num[b])
            b=b-size
        a=a+1
    print(" ".join(list(map(str,res)))+" ")