def h16():
    n = int(input())
    arr = list(map(int,input().split()))
    res = []
    temp = 0
    for i in range(n):
        if(arr[i]==1 and i!=0):
            res.append(temp)
            temp = 1
        else:
            temp += 1
        if(i==n-1):
            res.append(temp)
    l = len(res)
    print(l)
    for i in range(l-1):
        print(res[i],end=" ")
    print(res[l-1])

if __name__ == '__main__':
    h16()