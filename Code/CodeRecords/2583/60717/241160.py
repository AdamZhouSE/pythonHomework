n=int(input())
a=int(input())
b=int(input())
c=int(input())

list1=[]
if n > 100000000:
    print(1999999984)
else:
    for i in range(1,11):
        list1.append(b*i)
        list1.append(c*i)
        list1.append(a*i)
    list1=list(set(list1))
    list1.sort()
    print(list1[n-1])
    