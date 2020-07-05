n=int(input())
num1=list(input().split(" "))
num2=list(input().split(" "))
for i in range(len(num1)):
    num1[i]=int(num1[i])
for i in range(len(num2)):
    num2[i]=int(num2[i])
def reset(num,number):
    if num[0]==0:
        for i in range(1,number-1):
            num[i]=num[i+1]
        num[number-1]=-1
def compare(n):
    x=num1[0]
    y=num2[0]
    num1.pop(0)
    num2.pop(0)
    if(x+y)!=n:
        print(-1)
    else:
        a=0
        status=1
        while(num1[0]!=-1 and num2[0]!=-1):
            if(num1[0]<num2[0]):
                num2.append(num1[0])
                y+=1
                num2[y-1]=num2[0]
                num2[0]=0
                num1[0]=0
                x-=1
                reset(num2,y)
                reset(num1,x)
            else:
                num1.append(num2[0])
                x+=1
                num1[x-1]=num1[0]
                num2[0]=0
                num1[0]=0
                y-=1
                reset(num2,y)
                reset(num1,x)
            a+=1
            if a>n**2:
                status=0
                print(-1)
                break
        if status==1:
            if num1[0]==-1:
                print(a,2)
            if num2[0]==-1:
                print(a,1)
compare(n)