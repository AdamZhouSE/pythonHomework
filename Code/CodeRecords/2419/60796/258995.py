s=input()
ji=1
he=0
for i in range(len(s)):
    ji=ji*int(s[i])
    he=he+int(s[i])
print(ji-he)
