def alo(array,end,mid,result):
    count=0;
    for i in range(len(end)):
        if(mid[-1][i]!=end[i]):
            count+=1;
    if(count==1):
        if(end in array):
            result.append(mid+[end]);
        return result;
    else:
        for i in range(len(array)):
            if(len(array[i])==len(end)):
                count=0;
                for j in range(len(end)):
                    if(array[i][j]!=mid[-1][j]):
                        count+=1;
                if(count==1):
                    result=alo(array[i+1:],end,mid+[array[i]],result)
        return result;
begin=input();
end=input();
array=eval(input());
mid=[begin];
result=[];
result=alo(array,end,mid,result);
print(result)
a=len(min(result));
output=[];
for i in result:
    if(len(i)==a):
        output.append(i);
print(output)