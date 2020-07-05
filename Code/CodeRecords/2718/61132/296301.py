import functools

def merge(l1,l2):
    for i in l2:
        index2=0
        for j in l1:
            if i in j:
                l1[index2]+=[k for k in l2 if k not in l1[index2]]
                return l1
            index2+=1
    else:
        l1.append(l2)
        return l1

s=list(input())
l=eval(input())
l[0]=[l[0]]
#默认索引对中二值不等
l=functools.reduce(lambda x,y:merge(x,y),l)
for i in l:
    tmp=[]
    label=sorted(i[:])
    for j in label:
        tmp.append(s[j])
    tmp.sort()
    for j in range(len(tmp)):
        s[label[j]]=tmp[j]
print(''.join(s))