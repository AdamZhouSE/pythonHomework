def h28():
    n = int(input())
    arr = list(map(int,input().split()))
    arr.sort()
    if(len(arr)<3):
        print(len(arr))
    else:
        sum = arr[0] + arr[1]
        for i in range(2, n):
            isOver = False
            for j in range(i, n):
                if (arr[j] >= sum):
                    temp = arr[j]
                    arr[j] = arr[i]
                    arr[i] = temp
                    break
                if (j == n - 1):
                    isOver = True
            if(i==n-1 and not(isOver)):
                print(i+1)
                break
            elif(isOver):
                print(i)
                break
            sum += arr[i]


if __name__ == '__main__':
    h28()