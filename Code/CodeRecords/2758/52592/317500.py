
def count(n):
    s = count.cache.get(n, 0)
    if s:
        return s
    for k in range(n):
        s += count(k) * count(n - 1 - k)
        count.cache[n] = s
    return s

count.cache = {0 : 1}
s=input().split(' ')
a=int(s[0])
b=int(s[1])
print(count(a))
