T=int(input())
for i in range(0,T):
    arr=[int(n) for n in input().split(' ')]
    L,R=arr[0],arr[1]
    number=0
    while L<=R:
        str=bin(L)
        num=0
        for k in range(0,len(str)):
            if str[k]=='1':
                num=num+1
        if num == 1:
             L=L+1
        else:
            mark = 0
            for j in range(2, num - 1):
                if num % j == 0:
                    mark = 1
                    break
            if mark == 0:
               number= number + 1
            L=L+1
    print(number)
