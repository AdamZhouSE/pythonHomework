def isNumber(num):
    if num <=1:
        return False
    for i in range(2,int(num/2)+1):
        if num%i ==0:
            return False  #不是质数
    return True

numOfEx = int(input())

for i in range(numOfEx):
    n = input()
    lst = n.split(" ")
    one = int(lst[0])
    sec = int(lst[1])
    thi = 1
    while True:
        total = one + sec + thi
        if isNumber(total):
            break
        else:
            thi += 1
    print(thi)