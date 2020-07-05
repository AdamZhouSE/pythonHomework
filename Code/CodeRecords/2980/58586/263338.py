sentence=input()
line=input()
pattern=[]
for i in line:
    if not i.isspace():
        pattern.append(i)
if pattern[0]=="D":
    print(sentence.replace(pattern[1],"",1))
elif pattern[0]=="I":
    # print(pattern)
    temp=[c for c in sentence]
    idx=-1
    for c in range(len(temp)-1,-1,-1):
        if temp[c]==pattern[1]:
            idx=c
            break
    if idx==-1:
        print("no exist")
    else:
        temp.insert(idx,pattern[2])
    print("".join(temp))
elif pattern[0]=="R":
    if sentence.find(pattern[1])==-1:
        print("no exist")
        print(sentence)
    else:
        print(sentence.replace(pattern[1], pattern[2]))