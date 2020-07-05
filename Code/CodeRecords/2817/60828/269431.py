def h30():
    n = int(input())
    arr = list(map(int,input().split()))
    isExisted = False
    for i in range(n):
        if(arr[arr[arr[i]-1]-1] == i+1):
            isExisted = True
            break
    if(isExisted):
        print("YES")
    else:
        print("NO")


if __name__ == '__main__':
    h30()