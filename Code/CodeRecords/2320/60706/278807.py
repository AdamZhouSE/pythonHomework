S=input()
K=int(input())
ans=''
if K == 1:
    ans= min(S[i:] + S[:i] for i in range(len(S)))
else:
    ans="".join(sorted(S))
print(ans)