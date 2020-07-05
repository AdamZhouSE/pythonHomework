l=list(map(int,input().split(",")));
s=list(map(int,input().split(",")));
count=1;
while(True):
    judje=0;
    for j in s:
        for i in l:
            if ((i>=j)&(i<=(j+count)))  | ((i<j)&(i>=(j-count))):
                judje+=1;
    if(judje==len(l)):
        print(count);
        break;
    else:
        judje=0;
        count+=1;