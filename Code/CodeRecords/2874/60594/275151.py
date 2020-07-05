def jihua(n,num,jianshen,biancheng,i)->int:
    if i==n:
        return 0
    if num[i] == 0:
        biancheng = 0
        jianshen = 0
        return 1+jihua(n,num,jianshen,biancheng,i+1)
    elif num[i] == 1:
        if biancheng == 0:
            jianshen = 0
            biancheng = 1
            return jihua(n,num,jianshen,biancheng,i+1)
        else:
            biancheng = 0
            return 1+jihua(n, num, jianshen, biancheng, i + 1)
    elif num[i] == 2:
        if jianshen == 0:
            jianshen = 1
            biancheng = 0
            return jihua(n,num,jianshen,biancheng,i+1)
        else:
            jianshen = 0
            return 1+jihua(n,num,jianshen,biancheng,i+1)
    elif num[i] == 3:
        if jianshen == 0 and biancheng == 1:
            jianshen = 1
            biancheng = 0
            return jihua(n,num,jianshen,biancheng,i+1)
        if biancheng == 0 and jianshen == 1:
            biancheng = 1
            jianshen = 0
            return jihua(n,num,jianshen,biancheng,i+1)
        if biancheng == 0 and jianshen == 0:
            return min(jihua(n,num,1,0,i+1),jihua(n,num,0,1,i+1))
n = int(input())
num = [int(n) for n in input().split()]
print(jihua(n,num,0,0,0))