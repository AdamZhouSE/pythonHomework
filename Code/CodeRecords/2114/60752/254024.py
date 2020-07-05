import math
num=int(input())
add=0
min=-1
biggest=int(math.sqrt(num))
while biggest>0:
    n=num
    count=0
    i=biggest
    while n>0:
        if n>=i*i:
            n=n-i*i
            count+=1
        if n>=i*i:i=i+1
        i-=1
    biggest-=1
    if min==-1:min=count
    else:
        if min>count:min=count
print(min)