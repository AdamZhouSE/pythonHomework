times = int(input().split(" ")[1])
string = input()
for i in range(times):
    sub = input().split(" ")
    s1 = string[int(sub[0]):int(sub[1]) + 1]
    s2 = string[int(sub[2]):int(sub[3]) + 1]
    count = 0
    for j in range(min(len(s1), len(s2))):
        if s1[j] == s2[j]:
            count += 1
        else:
            break
    print(count)
