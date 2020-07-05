m = int(input(""))
st = " " + input("")
words = []
for i in range(0, m) :
    words.append(input(""))

n = len(st)
f = [100000007] * (n) ; f[0] = 0
for i in range(1, n) :
    for word in words :
        for j in range(0, len(word)) :
            if i <= j :
                break
            if ord(word[j]) == ord(st[i - j]) :
                f[i] = min(f[i], f[i - j - 1] + 1)
            else :
                break

print(f[n - 1])
