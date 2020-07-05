def count(num,n):
    count=0
    for i in num:
        if i==n:
            count+=1
    return count
def judge(num):
    for i in num:
        if count(num,i)>len(num)//2:
            return i
    return -1
T=int(input())
while T>0:
    n=int(input())
    num = [int(n) for n in input().split()]
    print(judge(num))
    T-=1