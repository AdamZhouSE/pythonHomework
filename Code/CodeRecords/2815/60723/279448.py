num=int(input())
temp=input().split()
cou=1
result=0
for i in range(num):
    number=int(temp[i])
    if abs(1-number)>abs(-1-number):
        cou=cou*(-1)
        result=result+abs(-1-number)
    elif abs(1-number)<abs(-1-number):
        result=result+abs((1-number))
if cou==-1:
    if temp.count('0')%2==0:
        result=result+temp.count('0')+2
    else:
        result=result+temp.count('0')
else:
    if temp.count('0')%2==0:
        result=result+temp.count('0')
    else:
        result=result+temp.count('0')
print(result)