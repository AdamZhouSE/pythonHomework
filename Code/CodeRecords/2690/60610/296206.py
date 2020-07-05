def alo(last,need,string,count):
    if(need==last):
        for i in range(len(string)):
            if(string[i]==need[0]):
                count+=1;
    else:
        for i in range(len(string)):
            if(string[i]==need[0]):
                count=alo(last,need[1:],string[i+1:],count);
    return count;

num=int(input());
length=input().split();
string=input().split();
count=0;
count=alo(string[1][-1],string[1],string[0],count);
print(count)