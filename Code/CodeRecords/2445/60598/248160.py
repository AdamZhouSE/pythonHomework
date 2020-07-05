s = input()
t = input()
if len(s) != len(t):
    print(False)
else:
    result = True
    S = [0 for x in range(26)]
    T = [0 for x in range(26)]
    for i in range(len(s)):
        S[ord(s[i])-ord('a')] += 1
        T[ord(t[i])-ord('a')] += 1
    for j in range(26):
        if S[j] != T[j]:
            result = False
            break
    print(result)
