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
Target=int(input());
Target-=1;

i=0;
count=0;
while(i<Target):
    count=2*count+1;
    i+=1;
i=0;
ans=[];
try:
    while(i<pow(2,Target)):
        ans.append(list[count+i]);
        i+=1;
    if(ans==[]):
        print("EMPTY");
    else:
        i=0;
        while(i<len(ans)-1):
            print(ans[i],end=" ");
            i+=1;
        print(ans[len(ans)-1]);
except Exception as e:
    if (ans == []):
        print("EMPTY");
    else:
        i = 0;
        while (i < len(ans) - 1):
            print(ans[i], end=" ");
            i+=1;
        print(ans[len(ans) - 1]);