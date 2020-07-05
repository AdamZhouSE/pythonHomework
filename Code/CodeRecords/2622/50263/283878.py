char = []
n = eval(input())
count = [1]*(len(n))
for i in range(len(n)):
    if n[i] not in char:
        char.append(n[i])
    else:
        for j in range(len(char)):
            if char[j] == n[i]:
                count[j] += 1
for i in range(len(count)):
    if count[i] > len(n)/2:
        print(char[i])