m = int(input(""))
st = input("")
words = []
for i in range(0, m) :
    words.append(input(""))

n = len(st) + 1
f = [10000007] * n ; f[0] = 0
for i in range(1, n) :
    now = st[0 : i]
    
    for word in words :
        for j in range(0, len(word)) :
            if i <= j :
                break
            if now.endswith(word[0 : j + 1]) :
                f[i] = min(f[i], f[i - j - 1] + 1)
    
print(f[n - 1])
