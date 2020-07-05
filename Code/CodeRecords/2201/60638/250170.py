def isPara(num):
    if num==1:
        return False
    for i in range(2,num):
        if num%i==0:
            return False
    return True
n=int(input())
for x in range(0,n):
    list1=list(map(int, input().split(" ")))
    num=list1[0]+list1[1]
    number=num+1
    while not isPara(number):
        number=number+1
    print(number-num)