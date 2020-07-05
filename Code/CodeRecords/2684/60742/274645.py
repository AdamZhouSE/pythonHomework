#minTime(r)表示0~r这一段中的最短时间
def minTime(r):
    if r<0:
        return 0
    elif r==0:
        return 0
    else:
        return min(minTime(r-1)+a[r],minTime(r-2)+a[r-1])

t = int(input())
for k in range(t):
    n = int(input())
    a = [int(i) for i in input().split()]
    time = minTime(n-1)
    print(time)