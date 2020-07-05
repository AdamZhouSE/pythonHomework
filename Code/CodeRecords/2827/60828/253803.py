def h8():
    n = int(input())
    arr = list(map(int,input().split()))
    n = len(arr)
    for i in range(n-2,-1,-1):
        for j in range (n-1,i-1,-1):
            if(arr[i]>arr[j]):
                temp = arr[i]
                arr[i] = arr[j]
                arr[j] = temp
    for i in range(n):
        if(i!=n-1):
            print(arr[i],end=" ")
        else:
            print(arr[i])


if __name__ == '__main__':
    h8()
