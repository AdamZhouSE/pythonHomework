string=input()
pairs=list(map(str,input()[2:-2].split("],[")))
changeable=[]
letters=[]
print(pairs)
for pair in pairs:
    x,y=map(int,pair.split(","))
    if(not changeable):
        changeable.append(set(x,y))
        letters.append([string[x],string[y]])
    else:
        for i in range(len(changeable)):
            k=0
            if(changeable[i] & set(x,y)):
                changeable[i]=changeable | set(x,y)
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
print(changeable)
for i in range(len(changeable)):
    letters[i].sort()

for s in string:
    k=0
    for letter in letters:
        if s in letter:
            k=1
            print(letters)
            print(letter.pop(0),end="")
            break
    if(k==0):
        print(s,end="")
            