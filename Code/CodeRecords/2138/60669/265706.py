def check():
    for i in range(0,len(arr)-1):
        temp=arr[i]
        for j in range(1,len(arr)-i):
            temp+=arr[i+j]
            if temp%k==0:
                return True
    return False


if __name__ == '__main__':
    arr = list(map(int, input().split(",")))
    k = eval(input())
    print(check())