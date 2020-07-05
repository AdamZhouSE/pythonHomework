string=list(input(""))
list=input("")[1:-1]
list=list+","
value=[]
for i in range(len(string)):
    value.append(ord(string[i]))
source=[]
for i in range(int(len(list)/6)):
    source.append([list[6*i+1],list[6*i+3]])
unions=[]
for i in range(len(source)):
    union=[]
    union.append(source[i][0])
    union.append(source[i][1])
    for i in range(len(source)):
        for a in range(len(source)):
            if((source[a][0] in union)|(source[a][1] in union)):
                if(not source[a][0] in union):
                    union.append(source[a][0])
                if(not source[a][1] in union):
                    union.append(source[a][1])
    union.sort()
    if(not union in unions):
        unions.append(union)
results=[]
for i in range(len(unions)):
    result=[]
    for a in range(len(unions[i])):
        result.append(value[int(unions[i][a])])
    result.sort()
    results.append(result)
answer=[]
for i in range(len(value)):
    answer.append(0)
for i in range(len(unions)):
    for a in range(len(unions[i])):
        answer[int(unions[i][a])]=results[i][a]
ans=""
for i in range(len(answer)):
    ans=ans+chr(answer[i])
print(ans)