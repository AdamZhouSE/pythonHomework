list1=eval(input())
for i in range(0,len(list1)):
    list1[i]=int(list1[i])
n=int(input())
flag=0
for i in range(0,len(list1)):
    if n==list1[i]:
        print(i)
        flag=1
if flag==0:
    print(-1)