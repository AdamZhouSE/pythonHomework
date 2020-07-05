num=eval(input())
num=sorted(num)

dis=0

if len(num)>=2:
    for i in range(len(num)-1):
        dis=max(dis, num[i+1]-num[i])
print(dis)