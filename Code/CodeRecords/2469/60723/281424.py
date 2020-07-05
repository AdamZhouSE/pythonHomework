T=int(input())
flag=True
for i in range(T):
    S=input()
    s=''
    for j in range(len(S)):
        if s.count(S[j])==0:
            s=s+S[j]
    window_length=len(s)
    while window_length<=len(S):
        for j in range(len(S)-window_length+1):
            flag=True
            temp=S[j:j+window_length]
            for k in range(len(s)):
                if temp.count(s[k])==0:
                    flag=False
            if flag:
                break
        if flag:
            print(window_length)
            break
        else:
            window_length=window_length+1