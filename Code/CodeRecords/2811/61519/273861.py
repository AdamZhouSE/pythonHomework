list1=list(input().split(" "))
n=int(list1[0])
ha=[int(list1[0])]
error=0
for i in range(n):
    ha.append(-1)
for i in range(int(list1[1])):
    num=int(input())
    x=num%n
    if ha[x]==1:
        print(i+1)
        error=1
        break
    else:
        ha[x]=1
if error==0:
    print(-1)