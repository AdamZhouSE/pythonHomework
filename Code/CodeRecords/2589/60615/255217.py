count=int(input())
list=[]

def lucas(n):
    if n==0:
        sum=2
    elif n==1:
        sum=1
    else:
        sum=lucas(n-1)+lucas(n-2)
    return sum

while count>0:  #count sub
    sum=0
    n=int(input())
    sum=lucas(n)
    list.append(sum)
    count=count-1
for i in list:
    print(i)