a=int(input())

i=0

while i<a:
    x=input().split(" ")
    result1=int(x[0])
    result2=int(x[1])
    result2=(1+result2)*result2/2
    if(result2>result1):
        print(0)
    else:
        print(1)
    i=i+1