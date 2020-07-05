T=int(input())
for i in range(0,T):
    arr=[int(n) for n in input().split(' ')]
    i,num=arr[0],arr[1]
    str="0b"
    for j in range(0,num):
        str=str+"1"
    number=eval(str)
    number=number-i+1
    print(number)