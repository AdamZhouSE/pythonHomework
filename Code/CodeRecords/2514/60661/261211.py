s=input()
t=input()
temp=-1
for i in range(len(s)):
    rec=t.find(s[i],temp+1)
    if rec==-1:
        print(False)
        exit()
    temp=rec
print(True)