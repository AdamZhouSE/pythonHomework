def get_keys(d, value):
    return [k for k,v in d.items() if v == value]
test=list(input())
lst=[]
count={}
for x in test:
    if x!="[" and x!= "]" and x!=",":
        lst.append(x)
for x in lst:
    if x in count:
        count[x]+=1
    else:
        count[x]=1

print(get_keys(count,1))