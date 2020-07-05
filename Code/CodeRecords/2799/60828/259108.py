def h18():
    def gcd(a,b):
        MIN = 0
        Max = 0
        Max = max(a,b)
        Min = min(a,b)
        if(Max%Min==0):
            return Min
        else:
            temp = Min
            Min = Max%Min
            Max = temp
            return gcd(Max,Min)

    n = int(input())
    arr = list(map(int,input().split()))
    GCD = arr[0]
    for i in range(1,n):
        GCD = gcd(GCD,arr[i])
    for i in range(n):
        arr[i] = int(arr[i]/GCD)
    for i in range(n):
        if(not(arr[i]==2 or arr[i]==3 or (arr[i]%2==0 and arr[i]%3==0) or arr[i]==1)):
            print("NO")
            break
        if(i==n-1):
            print("YES")


if __name__ == '__main__':
    h18()