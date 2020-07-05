list0=input().split()
n=int(list0[0])
l=int(list0[1])
lst=[]
for k in range(n):
    list1=input().split()
    list1[0] = int(list1[0])
    list1[1] = int(list1[1])
    lst.append(list1)
sum=0
s=0
for i in range(n):
    for j in range(i+1,n):
        dis=pow(lst[i][0]-lst[j][0],2)+pow(lst[i][1]-lst[j][1],2)
        if dis<pow(l,2):
            sum+=1
            s=(l-abs(lst[i][0]-lst[j][0]))*(l-abs(lst[i][1]-lst[j][1]))
if sum>1:
    print(-1)
elif sum==1:
    print(s)
else:
    print(0)