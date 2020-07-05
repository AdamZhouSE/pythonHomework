res1=1
list1=[1]
for i in range(0,30):
    res1=res1*10+1
    list1.append(res1)
n=int(input())
flag=False
for i in list1:
    if i%n==0:
        print(len(i))
        flag=True
        break
if flag==False:
    print(-1)