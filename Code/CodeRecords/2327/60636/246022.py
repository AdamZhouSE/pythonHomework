source=list(input())
number=[]
for i in range(len(source)+1):
    number.append(i)
res=[]
for i in source:
    if((i=="I")|(i=="W")):
        res.append(min(number))
        number.pop(0)
    elif(i=="D"):
        res.append(max(number))
        number.pop(-1)

res.append(number[0])
print(res)