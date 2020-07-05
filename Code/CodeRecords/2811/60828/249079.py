def h_3_2():
    p,n = input().split(" ")
    p = int(p)
    n = int(n)
    arr = []
    for i in range(0,p):
        arr.append(0)
    for i in range(0,n):
        x = int(input())%p
        if(arr[x]==1):
            print(i+1)
            break
        arr[x] = 1
        if(i==n-1):
            print(-1)

if __name__ == '__main__':
    h_3_2()