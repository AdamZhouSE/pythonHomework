T = int(input())
for _ in range(T):
    S = input()
    length = 1
    max_len = 1
    for i in range(len(S) - 1):
        if S[i] < S[i+1]:
            length += 1
        else:
            if max_len < length:
                max_len = length
            length = 1
    print(max_len)
