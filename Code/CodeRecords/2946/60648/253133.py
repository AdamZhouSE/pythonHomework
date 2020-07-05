n=input()
if n[-1]=='0':
    x=1
else:
    x=0
for i in range(len(n)-1):
    if n[i]!=n[i+1]:
        x+=1
print(x)