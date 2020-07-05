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
def boundList(x,y,bound):
    temp=0;
    ans=[];
    while(temp<=bound):
        i=0;
        j=0;
        while(x**i+y**j<=temp):
            if(x**i+y**j==temp):
                if(ans==[]):
                    ans.append(temp)
                elif(temp!=ans[len(ans)-1]):
                    ans.append(temp);
            else:
                while(x**i+y**j<=temp):
                    if (x ** i + y ** j == temp):
                        if (ans == []):
                            ans.append(temp)
                        elif (temp != ans[len(ans) - 1]):
                            ans.append(temp);

                    j+=1;
            j=0;
            i+=1;
        temp+=1;
    ans=quickSort(ans);
    print(ans);



x=int(input());
y=int(input());
bound=int(input());
boundList(x,y,bound);