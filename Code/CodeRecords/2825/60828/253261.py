def h_3_7():
    n = int(input())
    arr = []
    for i in range(n):
        temp = list(map(int,input().split()))
        sum = 0
        for j in range(len(temp)):
            sum += temp[j]
        arr.append(sum)
    rank = 1
    for i in range(1,n):
        if(arr[i]>arr[0]):
            rank += 1
    print(rank)

if __name__ == '__main__':
    h_3_7()