def h9():
    def cal_sta(arr):
        sta = 0
        l = len(arr)
        if(l==1):
            return 0
        for i in range(l):
            for j in range(i + 1, l):
                temp = max(arr[i] - arr[j], arr[j] - arr[i])
                sta = max(sta, temp)
        return sta

    n = int(input())
    arr = list(map(int,input().split()))

    arr_copy = arr[:]
    arr.remove(arr[0])
    sta = cal_sta(arr)

    for i in range(1,n):
        arr = arr_copy[:]
        arr.remove(arr[i])
        sta = min(sta,cal_sta(arr))
    print(sta)

if __name__ == '__main__':
    h9()