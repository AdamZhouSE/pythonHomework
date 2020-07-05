arr=list(input())
count=[0]*10
count[0]=arr.count('z')
count[2]=arr.count('w')
count[4]=arr.count('u')
count[6]=arr.count('x')
count[8]=arr.count('g')
count[1]=arr.count('o')-count[0]-count[2]-count[4]
count[3]=arr.count('r')-count[4]-count[0]
count[5]=arr.count('f')-count[4]
count[7]=arr.count('s')-count[6]
count[9]=arr.count('i')-count[5]-count[6]
for i in range(10):
    print(count[i]*str(i),end='')
print()