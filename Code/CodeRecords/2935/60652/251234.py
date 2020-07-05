s = list(''.join(input()))
index_Q = []
length = len(s)
for i in range(0, length):
    if s[i] == 'Q':
        index_Q.append(i)
num = 0
if len(index_Q) < 2:
    print(num)
else:
    for n in range(0, len(index_Q) - 1):
        for m in range(n + 1, len(index_Q)):
            num += s[index_Q[n]:index_Q[m]].count('A')
    print(num,end="")      