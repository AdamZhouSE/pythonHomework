# lengths = input().split(' ')
# aLen = int(lengths[0])
# bLen = int(lengths[1])
input()
a = input().split(' ')
a = [int(x) for x in a]
b = input().split(' ')
b = [int(x) for x in b]

out = []

for e in b:
    num = 0
    for i in a:
        if i <= e:
            num += 1
    out.append(num)

out = [str(x) for x in out]
out = ' '.join(out)
print(out)