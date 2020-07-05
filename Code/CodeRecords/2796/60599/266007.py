def wq(k):
    for i in range(1,k//2+1):
        if(i*i==k):
            return True
    return False

n=int(input())
s=list(map(int,input().split(' ')))
s.sort()
s.reverse()
for i in s:
    if(not wq(i)):
        if(i==0):
            print(-1)
            exit()
        print(i)
        exit()
