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
Total=makeIntList(input().split(" "));
list=makeIntList(input().split(" "));
size=Total[1];
i=0;
ans=[];
while(i<size):
    temp=makeIntList(input().split(" "));
    ans.append(min(list[temp[0]-1:temp[1]]));
    i+=1;
i=0;
while(i<len(ans)-1):
    print(ans[i],end=" ");
    i+=1;

print(ans[len(ans)-1],end=" ");