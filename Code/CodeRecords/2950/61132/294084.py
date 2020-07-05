s=list(input().split()[0])
tf=0
Max=0
for i in s:
    if i=='2':
        tf+=1
    elif i=='5':
        tf-=1
    if tf<0:
        print(-1)
        break
    Max=max(Max,tf)
else:
    if tf!=0:
        print(-1)
    else:
        print(Max)