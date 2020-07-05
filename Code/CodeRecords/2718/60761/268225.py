string=input()
pairs=list(map(str,input()[2:-2].split("],[")))
changeable=[]
letters=[]
for pair in pairs:
    x,y=map(int,pair.split(","))
    if(not changeable):
        changeable.append([x,y])
        letters.append([string[x],string[y]])
    else:
        for i in range(len(changeable)):
            k=0
            if(x in changeable[i]):
                changeable[i].append(y)
                letters[i].append(string[y])
                k=1
                break
            elif(y in changeable[i]):
                changeable[i].append(x)
                letters[i].append(string[x])
                k=1
                break
        if(k==0):
            changeable.append([x,y])
            letters.append([string[x],string[y]])
changeable2=changeable[:]
j=0
while j <len(changeable):
    i=j+1
    while i <len(changeable):
        if(set(changeable[j]) & set(changeable[i])):
            letters[j]=list(set(letters[j]) | set(letters.pop(i)))
            changeable[j]=list(set(changeable[j]) | set(changeable.pop(i)))
        else:
            i+=1
    letters[j].sort()
    j+=1

for s in string:
    k=0
    for letter in letters:
        if s in letter:
            k=1
            letter.append(letter.pop(0))
            print(letter[-1],end="")
            break
    if(k==0):
        print(s,end="")
print()            