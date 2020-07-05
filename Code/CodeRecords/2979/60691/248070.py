s = input()
l = s.split()

mlen = len(l[0])
count = 0
for i in range(0, len(l)):
    if len(l[i]) > mlen:
        mlen = len(l[i])
        count = i

print(l[count])