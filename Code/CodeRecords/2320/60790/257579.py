S=input()
k=int(input())
if(k==1):
    print(min(S[i:] + S[:i] for i in range(len(S))))
else:
    print("".join(sorted(S)))
