n=int(input())
li=list(map(int,input().split()))
li=sorted(li)[::-1]
cars=0
while(len(li)>1):
    if li[0]+li[len(li)-1]>4:
        cars=cars+1
        del li[0]
    else:
        li[0]=li[0]+li[len(li)-1]
        del li[len(li)-1]
print(cars+1)
        