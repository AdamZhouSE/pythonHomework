s = input()
rec = []
for i in range(len(s)):
    rec.append([s[i:],i+1])
rec.sort()
for i in range(len(rec)):
    if i != len(rec)-1:
        print(rec[i][1],end=" ")
    else:
        print(rec[i][1])
    