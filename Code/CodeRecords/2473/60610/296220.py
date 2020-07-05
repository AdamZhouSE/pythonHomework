num=int(input());
for i in range(num):
    length=int(input());
    string=list(map(int,input().split()));
    result=0;
    while(length>0):
        for i in range(len(string)-length+1):
            mid=string[i:i+length];
            com=length*min(mid);
            if(com>result):
                result=com;
        length-=1;
    print(result)