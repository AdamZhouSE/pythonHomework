num = int(input())
for i in range(0,num):
    b = input()
    li = b.split(' ')
    n1 = int(li[0])
    n2 = int(li[1])
    if(n1//n2>2 or n1//n2==2):
        print(1)
    else:
        print(0)