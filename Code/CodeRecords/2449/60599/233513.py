s=input()
num=s.split(',')
t=input()
for i in range(len(num)):
    if(t==num[i]):
        print(i)
        exit()
print(-1)
