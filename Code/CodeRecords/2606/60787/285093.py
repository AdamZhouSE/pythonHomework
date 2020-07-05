num=eval(input())
t=int(input())
for i in range(0,len(num)):
    if t==num[i]:
        print(i)
        break
else:
    print(-1)