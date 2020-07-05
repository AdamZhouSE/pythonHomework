num=int(input())
list=[]
li=[]
for i in range(0,num):
    n=input()
    li=n.split(' ')
    k=int(li.pop())
    n=int(li.pop())
    list.append((k**(n-1)))
for k in list:
    print(k)
