times = int(input())
for i in range(times):
    num = int(input())
    if num%2 == 0:
        print(num//2)
    else:
        print((num+1)//2)
