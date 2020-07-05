N = int(input())
cnt = 1
l = [i+1 for i in range(N//2 + 1)]
i = 2
while i != N // 2 + 1:
    for j in range(len(l)-i+1):
        if sum(l[j:j+i]) == N:
            cnt += 1
    i += 1
print(cnt)
