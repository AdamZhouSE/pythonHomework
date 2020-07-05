def foo(s: str):
    vowel = ['a', 'e', 'i', 'o', 'u']
    while len(s) != 0 and s[0] not in vowel:
        s = s[1:]
    while len(s) != 0 and s[-1] in vowel:
        s = s[:-1]
    if len(s) == 0:
        return [-1]
    res = list(set(permutation(s)))
    return sorted([s for s in res if len(s) != 0 and s[0] in vowel and s[-1] not in vowel])

def permutation(s: str) -> list:
    if len(s) == 0 or len(s) == 1:
        return [s, '']
    else:
        temp = permutation(s[1:])
        return [s[0] + i for i in temp] + temp
    
for _ in range(eval(input())):
    print(*foo(input()))