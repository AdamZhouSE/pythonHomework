def h25():
    n = int(input())
    arr = list(map(int, input().split()))
    bound_max = []
    bound_min = []
    Max = arr[0]
    Min = arr[0]
    for i in range(n):
        if(arr[i]>Max):
            Max = arr[i]
        if(arr[i]<Min):
            Min = arr[i]
    for i in range(n):
        if(arr[i]==Max):
            bound_max.append(i)
        if(arr[i]==Min):
            bound_min.append(i)
    d_max = 0
    for i in range(len(bound_max)):
        d_max = max(bound_max[i],n-1-bound_max[i])
    d_min = 0
    for i in range(len(bound_min)):
        d_min = max(bound_min[i],n-1-bound_min[i])
    res = max(d_max,d_min)
    print(res)

if __name__ == '__main__':
    h25()
