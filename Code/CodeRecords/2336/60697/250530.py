t=int(input())
sizes=[]
nums=[]
for i in range(t):
    sizes.append(list(map(int,input().split(' '))))
    nums.append(list(map(int, input().split(' '))))
for i in range(t):
    size=sizes[i][0]
    k=sizes[i][1]
    num=nums[i]
    res=[]
    for j in range(len(num)-k+1):
        res.append(max(num[j:j+k]))
    for n in res:
        print(n,end=" ")
    print()

