sample = 'CODEFESTIVAL2016'
s = list(input())
sample = list(sample)
sum = 0
for i in range(16):
    if s[i] != sample[i]:
        sum = sum + 1
print(sum)