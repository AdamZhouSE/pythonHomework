n = int(input())

All = []
for i in range(n - 1):
    All.append(list(map(int, input().split())))

ques = int(input())

for q in range(ques):
    temp = list(map(int, input().split()))
    a = temp[0]
    b = temp[1]
    ans = 0
    while a != b:
        for x in All:
            if x[0] == a:
                ans ^= x[2]
                a = x[1]
                break
    print(ans)