T= int(input())
for i in range(T):
    n = int(input())
    res = 0
    while n!=0 :
        if(n%2==1):
            n -=1
        else:
            n//=2
        res+=1
    print(res)