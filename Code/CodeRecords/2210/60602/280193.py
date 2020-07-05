import numpy as np
def quickSort(list):
    if(len(list)>1):
        count=1;
        x=list[0];
        leftList=[];
        rightList=[];
        while(count<len(list)):
            if(int(list[count])>=int(x)):
                rightList.append(list[count]);
            else:
                leftList.append(list[count]);
            count+=1;
        leftList.append(x);
        return quickSort(leftList)+quickSort(rightList);
    else:
        return list;
def leftLeastNum(list):
    i=0;
    ans=[];
    while(i<len(list)):
        j=i-1;
        while(j>=0):
            if(list[j]<list[i]):
                ans.append(list[j]);
                break;
            j-=1;
        else:
            ans.append(-1);
        i+=1;
    i=0;
    while(i<len(ans)-1):
        print(ans[i],end=" ");
        i+=1;
    print(ans[len(ans)-1]);


def leastPart(S,T):
    try:
        i=0;
        temp=[];
        x=0;
        while(x<len(T)):
            temp.append([]);
            x+=1;
        while(i<len(T)):
            j=0;
            while(j<len(S)):
                if(T[i]==S[j]):
                    temp[i].append(j);
                j+=1;
            i+=1;
        size=0;
        ans=[];
        tempstack=[];
        allans=[];
        count=1;
        while(size<len(temp)):
            count*=len(temp[size]);
            size+=1;
        size=0;
        while(len(allans)<count):
            ans=[];
            while(size<len(temp)):
                ans.append(temp[size][0]);
                tempstack.append(temp[size][0]);
                temp[size].remove(temp[size][0]);
                size+=1;
            allans.append(ans);
            size=0;
            while(size<len(temp)):
                temp[size].append(tempstack[0]);
                tempstack.remove(tempstack[0]);
                size+=1;
            size=0;
        i=0;
        while(i<len(allans)):
            allans[i]=quickSort(allans[i]);
            i+=1;
        ansarr=np.var(allans[0]);
        tempi=0;
        i=0;
        while(i<len(allans)):
            if(np.var(allans[i])<=ansarr):
                ansarr=np.var(allans[i]);
                tempi=i;
            i+=1;
    
    
        anslist=allans[tempi];
        print(S[anslist[0]:anslist[len(anslist)-1]+1]);
    except Exception as e:
        print(-1);


Total=int(input());
i=0;
while(i<Total):
    S=input();
    T=input();
    leastPart(S,T);
    i+=1;