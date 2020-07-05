a = eval(input())
if(len(a)<=2):
    print(0)
else:
    dis = 0
    a = sorted(a)
    print(a)
    for i in range(len(a)-1):
        dis = max(dis,a[i+1]-a[i])
print(dis)
