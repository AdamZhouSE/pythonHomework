S=input()
T=input()
while S.count(T)!=0:
    for i in range(0,len(S)-len(T)+1):
        if S[i:i+len(T)]==T:
            S=S[:i]+S[i+len(T):]
if S=='':
    print('ha',end='')
else:
    print(S,end='')
