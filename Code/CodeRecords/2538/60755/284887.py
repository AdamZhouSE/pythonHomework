s = input()[1:-1].split(",")
for i in range(len(s)):
    s[i] = int(s[i])
s.sort()
for i in range(1,100):
    if s.count(i)==0:
        print(i)
        break