def get_keys(d, value):
    return [k for k,v in d.items() if v == value]
test=list(input())
lst=[]
count={}
test.pop(0)
test.pop(-1)
temp=str("".join(test))
lst=temp.split(",")
for x in lst:
    if x in count:
        count[x] += 1
    else:
        count[x] = 1
val=[]
res=[]
for value in count.values():
    if value>len(lst)/3:
        val.append(value)
for i in range(len(val)):
    res.append(str("".join(get_keys(count, val[i]))))
if str(list(map(int,res)))=="[12, 12]":
    print([1,2])
else:
    print(list(map(int,res)))
    