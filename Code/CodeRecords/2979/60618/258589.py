s=input().split()
length=len(s[0])
re=s[0]
for i in range(0,5):
    if len(s[i])>length:
        length=len(s[i])
        re=s[i]
print(re)
