def h22():
    n = int(input())
    arr = list(map(int,input().split()))
    l = 1
    templ = 1
    bound = 0
    for i in range(1,n):
        if(arr[i]>arr[i-1] and i == n-1):
            templ += 1
            if (templ > l):
                l = templ
                bound = i
        elif(arr[i] > arr[i - 1]):
            templ += 1
        else:
            if(templ>l):
                l = templ
                bound = i
            templ = 1
    res = []
    for i in range(l):
        res.append(arr[bound-l+1+i])
    print(l)

if __name__ == '__main__':
    h22()