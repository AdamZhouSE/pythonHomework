s2= input()
s1 = input()
len1 = len(s1)
len2 = len(s2)


for i in range(0, len1 - len2 + 1):
    j = i
    k = i + len2 - 1
    p = j
    while j <= p <= k:
        if s1[p] in s2:
            p += 1
        else:
            break
    if p == k + 1 and sorted(s1[j:k + 1]) == sorted(s2):
        print("True")
        break
else:
    print("False")