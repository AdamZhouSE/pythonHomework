S = input()
T = input()
num = S.find(T)
while num != -1:
    S = S[:num] + S[num + len(T):]
    num = S.find(T)
if S == '':
    print(T, end='')
print(S, end='')
