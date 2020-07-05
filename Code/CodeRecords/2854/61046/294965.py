test=input().split()
test=sorted(list(map(int, test)))
count={}
all=[]
for x in test:
    if x in count:
        count[x]+=1
    else:
        count[x]=1
for v in count.values():
    all.append(v)
if max(all)<4:
    print("Alien")
else:
    fin=set(test)
    if len(fin)==1 or str(all)=="[4, 2]" or str(all)=="[2, 4]":
        print("Elephant")
    else:
        print("Bear")