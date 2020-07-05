list=input();
list.sort(key=None,reverse=False);
if(len(list)<2):
    print(0);
else:
    result=0;
    for i in range(0,len(list)-1):
        sub=abs(list[i+1]-list[i]);
        if(sub>result):
            result=sub;
print(result);