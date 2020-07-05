def isGood(num,k):
    list=[]
    while num!=0:
        list.append(num%k)
        num=int(num/k)
    for i in range(len(list)):
        if list[i]!=1:
            return False
    return True

num=int(input())
for i in range(2,num):
    if isGood(num,i):
        print(i)
        break