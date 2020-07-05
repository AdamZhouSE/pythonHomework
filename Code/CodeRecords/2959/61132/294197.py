def findsubstr(prefix,le,li):
    if le:
        if le>len(li):
            return []
        tmp = []
        for i in range(len(li) - le + 1):
            tmp += findsubstr(prefix+li[i], le - 1, li[i+1:])
        return tmp
    else:
        return [prefix]


s2=list(input().split()[0])
s3=list(input().split()[0])
sum=0
for l in range(1,min(len(s2),len(s3))):
    for i in findsubstr('',l,s2):
        for j in findsubstr('',l,s3):
            if i==j:
                sum+=1
print(sum)