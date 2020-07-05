NM = input().split(" ")
n = int(NM[0])
m = int(NM[1])
words = []
for i in range(n):
    a = input()
    words.append(a)
for i in range(m):
    wide = input().split(" ")
    b = words[int(wide[0])-1:int(wide[1])]
    b.sort()
    print(b[-1])