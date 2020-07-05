s = list(input())
for i in range(len(s)):
    s[i] = int(s[i])
num = s[:]
num.sort(reverse = True)
if str(num)==str(s):
    print("".join(str(i) for i in s))
else:
    t = False
    n = 0
    for i in range(len(num)):
        for j in range(i,len(num)):
            if s[j]>s[i]:
                t = True
                n = i
                break
        if t:
            break
    print(max(s[i:]))