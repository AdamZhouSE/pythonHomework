n=int(input())
num=[]
for i in range(n):
    tem=list(input().split(" "))
    for i in range(2):
        tem[i]=int(tem[i])
    num.append(tem)
num.sort()
ans=0
number2=[]
for i in range(n):
    number=[]
    number1=[]
    tem=num[i]
    num.pop(i)
    for j in range(n-1):
        for k in range(2):
            for m in range(num[j][0],num[j][1]):
                number.append(m)
    number.sort()
    for j in range(len(number)):
        if number[j] not in number1:
            number1.append(number[j])
    number2.append(len(number1))
    num.append(tem)
    num.sort()
out=int(max(number2))
print(out,end="")