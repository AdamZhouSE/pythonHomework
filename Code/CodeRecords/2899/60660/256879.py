inp=int(input())
flag=0
for i in range(2,33):
    if 1<<i==inp:
        if i%2==0:
            print('true')
            flag=1
            break
if flag==0:
    print('false')