def h_3_3():
    n = int(input())
    arr = input().split(" ")
    arr_num = list(map(int,arr))

    Max = arr_num[0]
    for i in range (0,n):
        if(arr_num[i]>=Max):
            Max = arr_num[i]

    sum = 0
    for i in range(1,Max+1):
        for j in range (0,n):
            if (arr_num[j] == i):
                sum += 1
                break

    print(sum)

if __name__ == '__main__':
    h_3_3()