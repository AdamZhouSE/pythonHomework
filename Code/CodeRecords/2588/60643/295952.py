def findPrimes(n):
    lst = []
    for i in range(2, n):
        while n % i == 0:
            lst.append(i)
            n = n // i
            continue
    return lst

def solution(n):
    lst=findPrimes(n)
    l1=[]
    l2=[]
    for i in str(n):
        l1.append(int(i))
    for num in lst:
        num=str(num)
        if len(num)==1:
            l2.append(int(num))
        else:
            for i in num:
                l2.append(int(i))
    if sum(l1)==sum(l2):
        return 1
    else:
        return 0

if __name__=="__main__":
    n = int(input())
    for _ in range(n):
        m=int(input())
        res=solution(m)
        print(res)