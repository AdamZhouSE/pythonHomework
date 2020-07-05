num=int(input());
for i in range(num):
    length=int(input());
    string=input().split();
    result=[];
    count=1;
    mid=0;
    while(string!=[]):
        if (len(string) == 1):
            result.append(1);
            break;
        else:
            words = string[0];
            string.remove(string[0]);
        j=0;
        while(j<len(string)):
            for k in words:
                if(k in string[j]):
                    mid+=1;
            if(mid==len(string[j])):
                count+=1;
                string.remove(string[j]);
            else:
                j+=1;
            mid=0;
        result.append(count);
        count=1;
    print(" ".join(sorted(list(map(str,result)))));