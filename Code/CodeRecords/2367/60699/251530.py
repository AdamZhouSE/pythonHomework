res1=1
list1=[1]
for i in range(0,30):
    res1=res1*10+1
    list1.append(res1)
n=int(input())
for i in list1:
    if i%n==0:
        print(i)
        break
print(-1)