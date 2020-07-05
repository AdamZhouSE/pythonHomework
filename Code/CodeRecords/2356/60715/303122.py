def find(num):
    if len(num)<=2:
        return num[0]
    for i in range(1,len(num)-1):
        left=[]
        right=[]
        for j in range(i+1):
            left.append(num[j])
        for k in range(i,len(num)):
            right.append(num[k])
        if num[i]==sorted(left)[len(left)-1] and num[i]==sorted(right)[0]:
            return num[i]
    return -1
T=int(input())
while T>0:
    n=int(input())
    num=[int(n) for n in input().split()]
    print(find(num))
    T-=1