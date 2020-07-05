s = list(input())
for i in range(len(s)):
    s[i] = int(s[i])
num = s[:]
num.sort(reverse = True)
if str(num)==str(s):
    print("".join(str(i) for i in s))
else:
    t = False
    for i in range(len(num)):
        for j in range(i,len(num)):
            if s[j]>s[i]:
                print(i,j)
                print(s[i],s[j])
                t = True
                break
        if t:
            break
