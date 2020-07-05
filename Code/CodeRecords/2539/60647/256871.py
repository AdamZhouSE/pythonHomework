list=input()
num=0
j=0
for i in range(len(list)-1):
    if int(list[i+1])<int(list[i]):
        if num==0:
            num+=2
            j=i
        else:
            num=num+i-j
            j=i
print(num)
