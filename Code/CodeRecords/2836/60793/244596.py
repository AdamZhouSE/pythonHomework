a_len = int(input())
a = list(map(int, input().split(" ")))
tries = 0
for i in range(0, a_len):
    temp = a.sort()
    print(temp)
    print(a)