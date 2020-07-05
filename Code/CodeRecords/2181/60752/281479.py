ask=[]
num=int(input())
a1=int(input())
ask.append(a1)
i=[2,10]
add=[8]
for n in range(num-1):
    a2=int(input())
    ask.append(a2)
    a1=max(a1,a2)
count=2
while count<=a1:
    add.append(add[len(add)-1]+count*6)
    i.append(i[len(i)-1]+add[len(add)-1])
    count+=1
for a in ask:
    print(i[a-1])
