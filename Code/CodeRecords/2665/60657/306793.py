num=int(input())
arr=[]
def cal(x,y,z):
    goalkeeper=z
    consa=0
    consb=0
    for i in range(z,1,-1):
       if(x%i==0):
           consa+=1
           x-=1
    for i in range(z,1,-1):
        if(y%i==0):
            consb+=1
            y-=1
    print(consa,consb)
for i in range(num):
    arr=input().split(' ')
    arr=[int(x) for x in arr]
    cal(arr[0],arr[1],arr[2])

