s=input()[1:-1].split(",")
for i in range(len(s)): s[i]=int(s[i])
print(s.index(max(s)))