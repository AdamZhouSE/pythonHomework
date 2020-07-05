def h18():
    def gcd(a,b):
        Max = max(a,b)
        Min = min(a,b)
        if(Max%Min==0):
            return Min
        else:
            temp = Min
            Min = Max%Min
            Max = temp
            return gcd(Max,Min)

    def okay(a,b):
        GCD = gcd(a,b)
        a = int(a/GCD)
        b = int(b/GCD)
        if((gcd(3,a)==3 or gcd(2,a)==2 or a==1) and (gcd(3,b)==3 or gcd(2,b)==2 or b==1)):
            return True
        return  False

    n = int(input())
    arr = list(map(int,input().split()))
    isYes = True
    for i in range(n):
        for j in range(i+1,n):
            if(not okay(arr[i],arr[j])):
                isYes = False
                break
        if(not isYes):
            break
    if(isYes):
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    h18()