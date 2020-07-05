import itertools
def makeIntList(list):
    count = 0;
    while (count < len(list)):
        list[count] = int(list[count]);
        count += 1;
    return list;
def sonList(list):
    ans=0;
    j=1;
    while(j<=len(list)):
        for i in itertools.combinations(list, j):
                ans+=max(i)-min(i);
        j+=1;
    print(ans);

list=makeIntList(str(input()).split(","));
sonList(list);