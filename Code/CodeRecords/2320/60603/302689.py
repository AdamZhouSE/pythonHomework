def orderlyQueue(S, K):
    if K == 1:
        return min(S[i:] + S[:i] for i in range(len(S)))
    return "".join(sorted(S))
S=input()
K=int(input())
print(orderlyQueue(S, K))