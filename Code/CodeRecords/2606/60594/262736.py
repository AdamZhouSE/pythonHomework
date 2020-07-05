so=eval(input())
n=(int)(input())
cunzai=False
for index in range(len(so)):
    if so[index]==n:
        cunzai=True
        print(index)
        break
if cunzai==False:
    print(-1)