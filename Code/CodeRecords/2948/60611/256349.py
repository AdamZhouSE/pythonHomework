source=input()
DL=int(input())
s=""
for i in range(len(source)):
    assist=DL+ord(source[i])-ord("A")
    s=s+str(assist)
while len(s)>2 :
    tmp=""
    if s=="100":
        break
    for i in range(len(s)-1):
        tmp=tmp+str((int(s[i])+int(s[i+1]))%10)
    s=tmp
print(int(s),end="")