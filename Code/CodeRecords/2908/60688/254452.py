times=int(input());
result=[];
for i in range(times):
    temp=list(input().strip(' '));
    temp=sorted(temp);
    result.append(''.join(temp));
result=set(result);
print(len(result))