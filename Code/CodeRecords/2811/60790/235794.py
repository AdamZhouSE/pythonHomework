str=input().split()
p=int(str[0])
n=int(str[1])
list1=[-1]*p
j=True
for num in range(0,n):
    cou=int(input())
    if(list1[cou%p]==-1):
        list1[cou%p]=cou
    else:
        print(num+1)
        j=False
        break
if(j):
    print(-1)