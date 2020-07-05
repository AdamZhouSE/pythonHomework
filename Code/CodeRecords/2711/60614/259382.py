def test(first,second):
    wrong=0
    for i in range(len(first)):
        if first[i]!=second[i]:
            wrong+=1
    if wrong<3:
        return True
    else:
        return False
str=eval(input())
groups=[]
for i in str:
    groups.append([i])
i=0
while i<len(groups):
    j=0
    while j<len(groups[i]):
        k=i+1
        while k<len(groups):
            for l in groups[k]:
                if test(groups[i][j],l):
                    groups[i]=groups[i]+groups.pop(k)
                    k-=1
                    break
            k+=1
        j+=1
    i+=1
print(len(groups))