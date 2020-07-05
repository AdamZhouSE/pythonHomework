n = int(input())
string = input().split()
ai = []
for x in string:
    ai.append(int(x))
ai.sort()
maxone = ai[0]
A = []
count = 0
for x in ai:
    if x <= 2 * maxone:
        maxone = x
        count += 1
    else:
        A.append(count)
        count = 1
        maxone = x
A.append(count)
print(max(A))
