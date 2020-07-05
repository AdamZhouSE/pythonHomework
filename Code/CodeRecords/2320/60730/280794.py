S = input()
K = int(input())
str_min = S
if K == 1:
    for i in range(len(S)):
        str_min = min(str_min, S[i:] + S[:i])
    print(str_min)
    exit()
print("".join(sorted(list(S))))
