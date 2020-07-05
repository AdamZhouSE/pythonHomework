def h21():
    s = list(map(int,input().split()))
    n = s[0]
    m = s[1]
    arr = []
    for i in range(m):
        arr.append(0)

    for i in range(n):
        s = list(map(int,input().split()))
        k = s[0]
        for i in range(1,k+1):
            arr[s[i]-1]=1

    isAllOn = True
    for i in range(m):
        if(arr[i]==0):
            isAllOn = False
            break
    if(isAllOn):
        print("YES")
    else:
        print("NO")

if __name__ == '__main__':
    h21()