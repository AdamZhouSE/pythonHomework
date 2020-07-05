letterin=input().split(", ")
length=len(letterin)
letters=[]
letters.append(letterin[0][2])
for i in range(1,length):
    letters.append(letterin[i][1])
letter=input()
find=False
i=0
for i in range(0,len(letters)):
    if letters[i]>letter:
        find=True
        break
if find:
    print(letters[i])
else:
    print(letters[0])