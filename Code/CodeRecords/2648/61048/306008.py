def tree16():
    S=input()
    T=input()
    flag=True
    while(flag):

        for i in range(len(S)-len(T)+1):
            if S[i:i+len(T)]==T:
                S=S[0:i]+S[i+len(T):]
                continue
        flag=False
        for i in range(len(S)-len(T)-1):
            if S[i:i+len(T)]==T:
                flag=True

    print(S,end='')
    return

tree16()