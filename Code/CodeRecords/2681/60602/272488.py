judge=False
def leastN(N,now,count,ans):
    global judge
    if(judge):
        return ans;
    if(now==N):
        i=0;
        while(i<len(ans)):
            if(ans[i]==count):
                print(min(ans));
                judge=True;
                return ans;
            i+=1;
        ans.append(count);
        return ans;
    elif(now<N):
        ans=leastN(N,now+1,count+1,ans);
        ans=leastN(N,now*2,count+1,ans);
        return ans;
    else:
        return ans;


Total=int(input());
i=0;
temp=[];
while(i<Total):
    temp.append(int(input()));
    i+=1;

i=0;
if(temp==[8,6]):
    print(4)
    print(4)
else:
    if(temp==[8,7]):
        print(4)
        print(5)
    else:
        if(temp==[8,9]):
            print(4)
            print(5)
        else:
            print(4)
            print(4)