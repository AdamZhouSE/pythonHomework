#从输入中获取p,n
setting=input()
settings=setting.split(' ')
p=int(settings[0])
n=int(settings[1])
#从输入中获取x，并计算h的值存储在一个列表中
hs=[]
xs=[]
yes_or_no=True
for number in range(1,n+1):
    x=input()
    xs.append(x)
for num in range(0,n):
    h=int(xs[num])%p
    #判断是否冲突,如果冲突把标志改为False
    for q in range(0,len(hs)):
        if hs[q] == h:
            yes_or_no=False
            break
    #如果不冲突，把h加入列表；如果冲突，打印
    if yes_or_no:
        hs.append(h)
    else:
        print(num+1)
        break
if yes_or_no:
    print(-1)




