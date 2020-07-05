source=input()
l=source[1:-1].split(",")
s=set(l)
for i in range(len(s)):
    if source.count(s[i])!=3:
        print(s[i])
        break