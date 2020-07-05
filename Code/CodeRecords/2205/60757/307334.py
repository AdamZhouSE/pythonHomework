def cal(a,li):
    if a%2==1:
        return 0
    if a==0:
        return 1
    li=[1]
    for i in range(0,a,2):
        sum=0
        for j in range(0,i+2,2):
            sum+=li[j//2]*li[(i-j)//2]
        li.append(sum)
    return li[a//2]

t=int(input())
for i in range(t):
    a=int(input())
    li=[]
    print(cal(a,li))
