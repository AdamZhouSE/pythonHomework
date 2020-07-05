def maxdiv(num):
    if(num<12):
        return num
    else:
        return max(num,maxdiv(num//4)+maxdiv(num//3)+maxdiv(num//2))
t=int(input())
for i in range(t):
    n=int(input())
    print(maxdiv(n))
    