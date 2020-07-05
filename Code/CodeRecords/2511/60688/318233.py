def makeIntList(list):
    count = 0;
    ans=[];
    while (count < len(list)):
        try:
            ans.append(int(list[count]));
        except Exception as e:
            count+=1;
            continue;
        count += 1;
    return ans;
def judgeInteresting(list,S):
    K=int(len(list)/2);
    i=0;
    if(sum(list[0:K])<=S and sum(list[K:])<=S):
        return True;
    else:
        return False;

size=makeIntList(input().split(" "));
S=size[1];
size=size[0];
i=0;
list=[];
while(i<size):
    list.append(int(input()));
    i+=1;
i=0;
while(i<len(list)):
    j=i+2;
    while(True):
        if(j>len(list)):
            tempLen=j-i-2;
            break;
        if(not judgeInteresting(list[i:j],S)):
            tempLen=len(list[i:j])-2;
            break;
        j+=2;
    print(tempLen);
    i+=1;