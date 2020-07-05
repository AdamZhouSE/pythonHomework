import itertools

require=list(map(int,input().split(",")))
result=[]
for i in itertools.combinations(range(1,10),require[0]):
    if sum(i)==require[1]:
        result.append(list(i))
print(result)