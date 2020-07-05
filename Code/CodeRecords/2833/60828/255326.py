def h10():
    n = int(input())
    cola = list(map(int,input().split()))
    v = list(map(int,input().split()))

    sum_cola = 0
    for i in range(n):
        sum_cola += cola[i]

    Max = 0
    for i in range(n):
        temp1 = v[i]
        for j in range(i+1,n):
            temp2 = v[j]
            Max = max(Max,temp1+temp2)
    if(Max>=sum_cola):
        print("YES")
    else:
        print("NO")

if __name__ == '__main__':
    h10()