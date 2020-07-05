s1 = input().replace(" ", "")
s2 = input().replace(" ", "")
letters1l = [0 for i in range(26)]
letters2l = [0 for m in range(26)]
letters1b = [0 for n in range(26)]
letters2b = [0 for o in range(26)]
for s in s1:
    if 'a' <= s <= 'z':
        letters1l[ord(s) - ord("a")] += 1
    else:
        letters1b[ord(s) - ord("A")] += 1
for s in s2:
    if 'a' <= s <= 'z':
        letters2l[ord(s) - ord("a")] += 1
    else:
        letters2b[ord(s) - ord('A')] += 1
finish = False
for j in range(26):
    if letters1l[j] < letters2l[j] or letters1b[j] < letters2b[j]:
        print("NO",end="")
        finish = True
        break
if not finish:
    print("YES",end="")
