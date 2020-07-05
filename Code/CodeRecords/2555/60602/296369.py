def makeIntList(list):
    count = 0;
    ans=[];
    while (count < len(list)):
        try:
            ans.append(int(list[count]));
        except Exception as e:
            count+=1;
            continue;
        count += 1;
    return ans;
Total=int(input());
list=makeIntList(input().split(" "));
i=0;
count=0;
while(i<len(list)):
    j=i+1;
    while(j<len(list)):
        if(list[j]>list[i]):
            k=j+1;
            while(k<len(list)):
                if(list[k]>list[j]):
                    count+=1;
                k+=1;
        j+=1;
    i+=1;
print(count,end="");