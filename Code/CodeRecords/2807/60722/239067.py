string=input().split(" ")
n=int(string[0])
m=int(string[1])
box=input().split(" ")
key=input().split(" ")
oddbox=0
oddkey=0
evenbox=0
evenkey=0
max=0
for i in range(n):
    if int(box[i])%2==1:
        oddbox+=1
    else:
        evenbox+=1
for i in range(m):
    if int(key[i])%2==1:
        oddkey+=1
    else:
        evenkey+=1
if oddbox>evenkey:
    max+=evenkey
else:
    max+=oddbox
if evenbox>oddkey:
    max+=oddkey
else:
    max+=evenbox
print(max)