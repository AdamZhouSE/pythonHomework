num=eval(input())
b=bin(num)
flag=True
for i in range(1,len(b)):
    if b[i]==b[i-1]:
        flag=False
        break
print(flag)