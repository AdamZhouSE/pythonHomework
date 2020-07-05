arr = list(map(int, input().split(",")))
Alex, Lee = 0, 0
for i in range(len(arr) - 1):
    if arr[0] > arr[-1]:
        if i % 2 == 0:
            Alex += arr[0]
        else:
            Lee += arr[0]
        del arr[0]
    else:
        if i % 2 == 0:
            Alex += arr[-1]
        else:
            Lee += arr[-1]
        del arr[-1]
Lee += arr[0]
if Alex > Lee:
    print(True)
else:
    print(False)
