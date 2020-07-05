def abccString(n,string,countb,countc,count):
    if(len(string)<n):
        count=abccString(n,string+"a",countb,countc,count);
        if(countb<1):
            count = abccString(n, string + "b", countb+1, countc,count);
        if(countc<2):
            count = abccString(n, string + "c", countb, countc+1,count);
        return count;
    else:
        return count+1;

Total=int(input());
i=0;
while(i<Total):
    temp=int(input());
    print(abccString(temp,"",0,0,0));
    i+=1;