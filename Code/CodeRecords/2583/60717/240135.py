n=int(input())
a=int(input())
b=int(input())
c=int(input())

list1=[]

for i in range(0,10):
    for j in range(0,10):
        for k in range(0,10):
            list1.append((a**i)*(b**j)*(c**k))    
list1=list(set(list1))
list1.sort()
list1.remove(1)
print(list1[n-1])
    