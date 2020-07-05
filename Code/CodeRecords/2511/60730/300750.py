n, s = map(int, (input().strip().split(" ")))
temp = []
for i in range(n):
    temp.append(int(input()))
for j in range(n):
    if (n - j) % 2 == 0:
        cnt = 0
        while True:
            if n - cnt <= j:
                print(0)
                break
            if sum(temp[j:j + (n - j - cnt) // 2]) <= s and sum(temp[j:n - cnt]) - sum(
                    temp[j:j + (n - j - cnt) // 2]) <= s:
                print(n - j - cnt)
                break
            else:
                cnt += 2
    else:
        cnt = 0
        while True:
            if n - cnt - 1 <= j:
                print(0)
                break
            if sum(temp[j:j + (n - j - 1 - cnt) // 2]) <= s and sum(temp[j:n - 1 - cnt]) - sum(
                    temp[j:j + (n - j - 1 - cnt) // 2]) <= s:
                print(n - j - cnt - 1)
                break
            else:
                cnt += 2
