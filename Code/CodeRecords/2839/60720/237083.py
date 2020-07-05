size=int(input())
list=[0]*size

for i in range(size):
    isY=False
    list[i]=input()
    for j in range(i):
        if list[i]==list[j]:
            isY=True
    if(isY):
        print('YES')
    else:
        print('NO')