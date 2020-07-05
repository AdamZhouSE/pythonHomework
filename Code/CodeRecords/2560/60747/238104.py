n=int(input())
num1=[0for i in range(n)]
num2=[0for i in range(n)]
num3=[0for i in range(n)]

def dels(p,num2,num3):
    count = 0
    a=0
    while a!=-1:
        for i in num2:
            if num2.count(i)==p:
                count = count + 1
                num3 = num3 - p
                if num3==0:
                    a=-1
                    break
        p=p+1
    return count

for i in range(n):
    num1[i]=int(input())
    num2[i]=input().split(" ")
    num3[i]=int(input())
for i in range(n):
    print(len(set(num2[i]))-dels(1,num2[i],num3[i]))
