times=int(input());
result=[];
for i in range(times):
    temp=list(input());
    temp=sorted(temp);
    result.append(temp);
print(result)