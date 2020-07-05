t = int(input())
for i in range(t):
    arr = int(input())
    if int(arr ** (1 / 2)) == arr**(1/2):
        print(1)
    else:
        print(0)