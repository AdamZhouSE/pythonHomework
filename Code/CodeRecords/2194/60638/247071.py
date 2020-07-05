def isPara(num):
    if num==1:
        return False
    for i in range(2,num):
        if num%i==0:
            return False
    return True
n=int(input())
for i in range(0,n):
    numbers=list(map(int,input().split(" ")))
    num=0
    for num in range(numbers[0],numbers[1]+1):
        if isPara(num):
            print(num,end="")
            break
    for num in range(num+1,numbers[1]+1):
        if isPara(num):
            print("",num,end="")
    print()