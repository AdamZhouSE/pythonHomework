S=list(input())
K=int(input())
if K>=len(S):
    print(''.join(sorted(S)))
else:
    s1=max(S[:K],key=ord)
    s2=min(S[K:],key=ord)
    while s1>s2:
        S.remove(s1)
        S.append(s1)
        s1 = max(S[:K], key = ord)
        s2 = min(S[K:], key=ord)
    S[:K]=sorted(S[:K])
    print(''.join(S))