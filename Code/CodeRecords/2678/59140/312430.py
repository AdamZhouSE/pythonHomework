t=int(input())
for _ in range(t):
    temp=int(input())
    temp='{:032b}'.format(temp)
    if temp.count('1')==1:
        print(32-temp.index('1'))
    else:print(-1)