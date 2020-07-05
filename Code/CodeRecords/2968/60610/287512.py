string=input();
num=int(input());
for i in range(num):
    string1=input().split();
    if(string1[0]=="1"):
        string=string+string1[1];
    elif(string1[0]=="2"):
        string=string1[1][::-1]+string;
    else:
        count=0;
        for i in range(0,len(string)):
            for j in range(len(string)-i):
                mid=string[j:j+1+i];
                Rmid=mid[::-1];
                if(mid==Rmid):
                    count+=1;
        print(count);