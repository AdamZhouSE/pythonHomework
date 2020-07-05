str=input().split()
p=int(str[0])
n=int(str[1])
str={}
temp=0
for i in range(n):
    number=int(input())
    position=number%p
    if position in str:
        temp=1
        print(i+1)
        break
    else:
        str[position]=number
if temp==0:
    print('-1')