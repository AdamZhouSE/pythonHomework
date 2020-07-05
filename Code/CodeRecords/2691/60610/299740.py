def alo(array,mid,result):
    for i in range(len(array)):
        if(array[i] not in mid):
            if(mid+[array[i]] not in result):
                if(sum(mid+[array[i]]) not in result):
                    result.append(sum(mid+[array[i]]));
                    result=alo(array,mid+[array[i]],result)
    return result
num=int(input());
for i in range(num):
    length=int(input());
    nums=list(map(int,input().split()));
    mid=[];
    result=[];
    result=alo(nums,mid,result);
    output=sum(nums);
    for i in result:
        if(abs(i-sum(nums)/2)<output):
            output=abs(i-sum(nums)/2);
    print(int(output*2))