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

print(str("".join(get_keys(count, 1))))