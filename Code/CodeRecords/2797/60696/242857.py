n = int(input())
arr = [int(i) for i in input().split()]
if arr[-1] == 0:
    print('UP')
elif arr[-1] == 15:
    print('DOWN')
elif n == 1:
    print('-1')
else:
    if arr[-1] - arr[-2] > 0:
        print('UP')
    else:
        print('DOWN')