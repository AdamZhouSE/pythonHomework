num=int(input())
sp=input()[2:-2].split("],[")
sp_=[]
for i in range(len(sp)):
    sp_.append(list(map(int,sp[i].split(","))))
in_=set()
out_=set()
all=set()
for i in sp_:
    in_.add(i[0])
    out_.add(i[1])
    all.add(i[0])
    all.add(i[1])
sor=[]
len_=len(out_)
while(len(out_)!=0):
    for i in out_:
        if i not in in_:
            out_.remove(i)
            all.remove(i)
            sor.append(i)
            for j in sp_:
                if j[1]==i:
                    in_.discard(j[0])
            break
    if(len_==len(out_)):
        break
    else:len_ = len(out_)
if(len_==0):
    for i in all:
        sor.append(i)
    print(sor)
else:print("[]")
