num=list(input().split(" "))
money=list(input().split(" "))
res=[]
for i in range(int(num[1])):
    tem=list(input().split(" "))
    left=int(tem[0])
    right=int(tem[1])
    t=int(money[left-1])
    for j in range(left,right):
        if int(money[j])<=int(t):
            t=money[j]
    res.append(str(t))
s=" ".join(res)
print(s,end=" ")