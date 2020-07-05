def makeIntList(list):
    count = 0;
    while (count < len(list)):
        list[count] = int(list[count]);
        count += 1;
    return list;
def ThreeDItem(list):
    i=0;
    ans=0;
    while(i<len(list)):
        j=0;
        while(j<len(list[0])):
                count=1;
                while(count<=list[i][j] and list[i][j]!=0):
                    if(count==1):
                        ans+=1;
                    ans+=4;
                    try:
                        if(list[i+1][j]>=count):
                            ans-=1;
                    except Exception as e:
                        temp = 0;
                    try:
                        if (list[i][j+1] >= count):
                            ans -= 1;
                    except Exception as e:
                        temp = 0;
                    try:
                        if (i-1>=0 and list[i - 1][j] >= count):
                            ans -= 1;
                    except Exception as e:
                        temp = 0;
                    try:
                        if (j-1>=0 and list[i][j-1] >= count):
                            ans -= 1;
                    except Exception as e:
                        temp=0;
                    if(count==list[i][j]):
                        ans+=1;
                    count+=1;
                j+=1;
        i+=1;
    print(ans);


Total=int(input());
i=0;
list=[];
while(i<Total):
    list.append(makeIntList(str(input()).split(",")));
    i+=1;

ThreeDItem(list);