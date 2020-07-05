seq = eval(input())
seq = sorted(seq)
length = len(seq)
if length == 0:
    exit()
i = 1
ans = []
while i < length:
    if seq[i - 1][1] < seq[i][0]:
        i = i + 1
    else:
        tmp = ([seq[i - 1][0], seq[i][1]])
        seq = seq[2:]
        seq.insert(0, tmp)
        length = length - 1
print(seq)
