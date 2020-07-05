def same(sb, c):
    sb = sorted(list(sb))
    return sb == c

def test():
    S = input()
    C = sorted(list(input()))
    l = len(C)
    count = 0
    for i in range(len(S)-l+1):
        if same(S[i:i+l], C):
            count +=1
    result.append(count)

result = []
for i in range(int(input())):
    test()

for i in result:
    print(i)