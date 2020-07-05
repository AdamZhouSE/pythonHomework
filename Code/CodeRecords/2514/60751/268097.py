s=input()
t=input()
j=0
count=0
for i in s:
    while(j<len(t)):
        if t[j]==i:
            j+=1
            count+=1
            break
        else:
            j+=1
if count==len(s):
    print(True)
else:
    print(False)
