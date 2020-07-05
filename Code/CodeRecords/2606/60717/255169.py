list1=eval(input())
for i in range(0,len(list1)):
    list1[i]=int(list1[i])
n=int(input())
if n<list1[0] or n>list1[len(list1)-1]:
    print(-1)
for i in range(0,len(list1)):
    if n==list1[i]:
        print(i)