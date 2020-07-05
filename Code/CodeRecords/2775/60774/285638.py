t = int(input())
for i in range(0,t):
    num = int(input())
    mid = int(num / 3)
    if(3 * mid != num):
        print(-1)
    else:
        print(str(mid - 1) + ' ' + str(mid) + ' ' + str(mid + 1))