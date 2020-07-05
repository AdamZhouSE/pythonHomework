S=input()
K=int(input())
if K == 1:
    print(min(S[i:] + S[:i] for i in range(len(S))))
else:
    print("".join(sorted(S)))
