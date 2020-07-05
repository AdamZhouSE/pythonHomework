firstLine=input()
current=""
num=1
temp=0
for i in range(int(firstLine)):
    time=input()
    if time!=current:
        current=time
        temp=1
    else:
        temp+=1
        if num<temp:
            num=temp
print(num)