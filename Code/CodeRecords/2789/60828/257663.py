def h14():
    def cal_max(n,arr):
        arr.sort()
        max = 0
        for i in range(n):
            if(arr[(n-1)-i]<i+1):
                break
            max = i+1
        return max
    res = []
    k = int(input())
    for i in range(k):
        n = int(input())
        arr = list(map(int,input().split()))
        res.append(cal_max(n,arr))
    for i in range(k):
        print(res[i])

if __name__ == '__main__':
    h14()
