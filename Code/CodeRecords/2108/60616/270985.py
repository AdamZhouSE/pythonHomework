def countOne(num):
    s=''
    for i in range (num+1):
        s=s+str(i)
    return s.count('1')
num=int(input())
print(countOne(num))