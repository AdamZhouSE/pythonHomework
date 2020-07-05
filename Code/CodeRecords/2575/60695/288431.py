seq = input()
res = [0]*len(seq)
cnt = 0
for i, x in enumerate(seq):
    if x == "(":
        cnt += 1
        res[i] = cnt % 2
    else:
        res[i] = cnt % 2
        cnt -= 1
for i in range(0, len(seq)):
    if res[i] == 1:
        res[i]=0
    else:
        res[i]=1
print(res)
