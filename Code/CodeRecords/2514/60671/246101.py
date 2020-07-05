s=input()
t=input()
place=0
slen=len(s)
tlen=len(t)
count=0
for i in range(tlen):
    if(t[i]==s[place]):
        place+=1
        count+=1
if(count==(slen)):
    print(True)
else:
    print(False)