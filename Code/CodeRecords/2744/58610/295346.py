string = [input().split()[1] for _ in range(eval(input()))]
count = 0
for i in range(len(string)):
    s0 = string[i] + string[i]
    if s0 == s0[::-1]:
        count += 1
    for j in range(i + 1, len(string)):
        s1 = string[i] + string[j]
        s2 = string[j] + string[i]
        if s1 == s1[::-1]:
            count += 1
        if s2 == s2[::-1]:
            count += 1
print(count)