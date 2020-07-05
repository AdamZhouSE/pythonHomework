a=int(input())
zi=[2,3,5,7,11]
for k in range(0,a):
    result=0
    a=input().split(' ')
    qi=int(a[0])
    zhong=int(a[1])
    for i in range(qi,zhong+1):
        temp=0
        str=bin(i)
        str=str.replace("0b","")
        for j in range(0,len(str)):
            if str[j]=='1':
                temp=temp+1
        if temp in zi:
            result=result+1
    print(result)