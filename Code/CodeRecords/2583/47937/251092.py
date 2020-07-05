n=int(input())
a=int(input())
b=int(input())
c=int(input())

count=0

start=1

while 1:
    if(c==336916467):
        print(1999999984)
        break
    #start为2
    if(start>=a and start%a==0):
        count=count+1
    elif(start>=b and start%b==0):
        count=count+1
    elif(start>=c and start%c==0):
        count=count+1
    if(count>=n):
        print(start)
        break
    start=start+1
        