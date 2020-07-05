def h29():
    n = int(input())
    arr = list(map(int,input().split()))
    arr.sort()
    for i in range(n-1):
        if(i%2==0):
            arr.remove(arr[len(arr)-1])
        else:
            arr.remove(arr[0])
    print(arr[0])

if __name__ == '__main__':
    h29()