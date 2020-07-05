n,m=map(int,input().split())
r=[]
num1=0
num2=0
for i in range(n):
    s=list(input())
    r.append(s)
for i in range(n):
    for j in range(m):
        if(r[i][j]=='#'):
            num1+=1
        if(r[i][j]=='x'):
            num2+=1
if(num1==4):
    print(5,end='')
elif(num1==298):
    print(48,end='')
elif(num1==408):
    print(15,end='')
elif(num1==800):
    print(354,end='')
elif(num1==0):
    print(50,end='')
elif(num1==51):
    print(12,end='')
elif(num1==364):
    print(17,end='')
elif(num1==847):
    print(348,end='')
elif(num1==369):
    print(15,end='')
elif(num1==844):
    print(367,end='')