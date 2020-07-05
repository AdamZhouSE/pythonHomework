num = int(input())
for i in range(num):
    n, m = list(map(int, input().split(" ")))
    arr = sorted(list(map(int, input().split(" "))), reverse=True)
    for item in arr[:m]:
        print(item,end=" ")
    print()
