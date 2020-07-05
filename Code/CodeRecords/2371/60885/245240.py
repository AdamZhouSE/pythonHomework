gap = ord('a') - ord('A')

def test():
    S = list(input())
    l,r = 0, len(S)-1
    while l < r:
        if not S[l].isalpha():
            l += 1
        elif not S[r].isalpha():
            r -= 1
        else:
            temp = abs(ord(S[l]) - ord(S[r]))
            if not temp == 0 and not temp == gap:
                result.append('NO')
                break
            l += 1
            r -= 1
    else:
        result.append('YES')

result = []
for i in range(int(input())):
    test()

for i in result:
    print(i)