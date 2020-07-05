t=int(input())
for _ in range(t):
    temp=int(input())
    temp='{:032b}'.format(temp)
    temp=list(temp)
    for i in range(32):
        temp[i]=str((int(temp[i])+1)%2)
    temp='0b'+''.join(temp)
    print(int(temp,2))