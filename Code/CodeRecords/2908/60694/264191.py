
N = int(input())
words = [input() for _ in range(N)]
aSet = set()
for word in words:
    word = "".join((lambda x: (x.sort(), x)[1])(list(word)))
    aSet.add(word)
    
print(len(aSet), end="")
