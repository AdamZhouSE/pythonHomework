n = int(input())
s1 = input()

l1 = []

for i in range(len(s1)):
    if not s1[i] in l1:
        l1.append(s1[i])

s = "".join(l1)
print(s)
