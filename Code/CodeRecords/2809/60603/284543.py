num=int(input())
list=input().split(" ")
for i in range(num):
    list[i]=int(list[i])
list.sort()
if(num%2==0):
    num1=0
    num2=0
    for i in range(0,int(num/2)):
        num1+=list[i]
    for i in range(int(num/2),num):
        num2+=list[i]
    print(num1*num1+num2*num2)
else:
    num1 = 0
    num2 = 0
    for i in range(0, int(num/2)):
        num1 += list[i]
    for i in range(int(num/2), num):
        num2 += list[i]
    ans1=num1 * num1 + num2 * num2
    num1 = 0
    num2 = 0
    for i in range(0, int(num/2)+1):
        num1 += list[i]
    for i in range(int(num/2)+1, num):
        num2 += list[i]
    ans2=num1* num1 + num2 * num2
    if(ans1>ans2):
        print(ans1)
    else:
        print(ans2)