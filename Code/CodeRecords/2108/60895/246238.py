n=int(input())
num=0
if n>20:
    num=num+(n-21)//10+1
    n=19
while n>=12:
    num=num+1
    n=n-1
num=num+4
print(num)