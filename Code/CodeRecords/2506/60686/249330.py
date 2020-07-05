list_input = input().split(",")
for i in range(len(list_input)):
    list_input[i] = int(list_input[i])
if not list_input:
    print(0)
else:
    dp = [1] * len(list_input)
    for i in range(1, len(list_input)):
        for j in range(i):
            if list_input[i] > list_input[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    print(max(dp))
