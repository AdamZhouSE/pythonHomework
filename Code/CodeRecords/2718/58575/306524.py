words=list(input())
pairs=input()[1:-1]
pair=[]
res=[]

def cal(word):
    flag=False
    for i in pair:
        tmp=word.copy()
        tmp[i[0]],tmp[i[1]]=tmp[i[1]],tmp[i[0]]
        if tmp not in res:
            res.append(tmp)
            cal(tmp)
            flag=True

    if flag==False:
        return
i=0
while i<len(pairs):
    if pairs[i]=='[':
        j=pairs[i:].index("]")+i
        temp=list(map(int,pairs[i+1:j].split(",")))
        pair.append(temp)
        i=j+1
    i+=1

cal(words)
res.sort()
print("".join(res[0]))