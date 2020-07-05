def findsubstr2(s,le,li):
    tmp=[]
    index=0
    while index+le<=len(li):
        tmp.append(''.join(li[index:index+le]))
        index+=1
    return tmp

s2=list(input().split()[0])
s3=list(input().split()[0])
sum=0
for l in range(1,min(len(s2),len(s3))+1):
    for i in findsubstr2('',l,s2):
        for j in findsubstr2('',l,s3):
            if i==j:
                sum+=1
print(sum)