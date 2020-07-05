n=int(input())
list1=input().split()
list1=[int(x) for x in list1]
list1.sort()
s=0
for i in range(n-1):
    while (list1[i]==list1[i+1]):
        list1[i+1]+=1
        s+=1
        list1.sort()
print(s)        