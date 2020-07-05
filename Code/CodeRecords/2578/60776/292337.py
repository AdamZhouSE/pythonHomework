a=input()
b=a.split(',')
for i in range(0,len(b)):
    b[i]=int(b[i])
chushu=int(input())
for i in range(0,len(b)):
    if b[i]%chushu!=0:
        b[i]=int(b[i]/chushu)+1
    else:
        b[i]=int(b[i]/chushu)
print(sum(b))