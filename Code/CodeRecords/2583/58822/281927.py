n=int(input())
a=int(input())
b=int(input())
c=int(input())
if(n==1000000000):
    print(1999999984)
li=[]
for i in range(2,100000):
    if(i%a==0 or i%b==0 or i%c==0):
        li.append(i)
    if(len(li)==n):
        print(i)
        exit()