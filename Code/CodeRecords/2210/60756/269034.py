T=int(input())
for t in range(T):
    S=list(input())
    T=list(input())
    flag=True
    for L in range(len(T),len(S)+1):
        for i in range(0,len(S)-len(T)):
            temp=S[i:i+L]
            flag=True
            for c in T:
                if c not in temp:
                    flag=False
                    break
            if flag:
                print(''.join(temp))
                break
        if flag:
            break
    if not flag:
        print(-1)
        print()