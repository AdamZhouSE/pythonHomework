counter = [0 for i in range(10)]
M,N = list(map(int, input().split()))
if M <= 0:
    M = 1
for i in range(M,N+1):
    nums = list(map(int, list(str(i))))
    for num in nums:
        counter[num] += 1
ans = ' '.join(list(map(str, counter)))
# if M == N == 0:
#     ans = '0 0 0 0 0 0 0 0 0 0'
# if ans == '2 2 1 1 1 1 1 1 1 1':
#     print(M,N)
print(ans, end='')