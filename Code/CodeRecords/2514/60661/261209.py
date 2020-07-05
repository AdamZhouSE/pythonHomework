s=input()
t=input()
temp=-1
for i in range(len(s)):
    rec=t[temp+1:].find(s[i])
    if rec==-1:
        print(False)
        exit()
    temp=rec
print(True)