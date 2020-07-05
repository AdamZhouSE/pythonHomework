inp = input().split(" ")
K, M = int(inp[0]), int(inp[1])
S = input()
N = int(input())
for i in range(N):
    inp = input().split(" ")
    A, B, C = int(inp[0]), int(inp[1]), int(inp[2])
    copy = S[A:B]
    S = S[0:C] + copy + S[C:]
    if len(S) > M:
        S = S[0:M+1]
print(S[0:K], end="")
