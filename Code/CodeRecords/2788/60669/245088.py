n=int(input())
ai=list(map(int,input().split()))
m=int(input())
bi=list(map(int, input().split()))
result=0

if n<=m:
    less=ai
    more=bi
else:
    less=bi
    more=ai

record=0
strength=len(less)-1
for skill in less:
    equal=more.count(skill)
    add=more.count(skill + 1)
    sub=more.count(skill - 1)
    if equal!=0:
        more.remove(skill)
        result+=1
    else:
        if add!=0 and sub!=0 and record<=strength:
            less.append(skill)
        else:
            if add==0:
                if sub==0:
                    continue
                else:
                    more.remove(skill - 1)
                    result+=1
            else:
                more.remove(skill+1)
                result+=1
    record+=1
# if result==4:
#     print(ai)
#     print(bi)
# else:
#     print(result)
print(result)