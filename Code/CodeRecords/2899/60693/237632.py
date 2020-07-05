num=int(input())
tmp=num
flag=1
while(tmp!=0):
    if tmp==1:
        break
    if tmp%4!=0:
        flag=0
        break
    else:
        tmp=int(tmp/4)
if flag==1:
    print('true')
else:
    print('false')