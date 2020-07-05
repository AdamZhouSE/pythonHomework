read = lambda: eval(input())
read_line = lambda: [int(x) for x in input().split()]


def is_anagram(a, b):
    d1, d2 = {}, {}
    for x in a:
        d1[x] = d1[x] + 1 if x in d1 else 1
    for x in b:
        d2[x] = d2[x] + 1 if x in d2 else 1
    return d1 == d2


tmp = input()
a = tmp.find('"')
b = tmp.find('"', a + 1)
c = tmp.find('"', b + 1)
d = tmp.find('"', c + 1)
s = tmp[a + 1:b]
t = tmp[c + 1:d]
print('true' if is_anagram(s, t) else 'false')
