def editNum(string,num):
    i=0;
    list=[];
    while(i<len(string)):
        list.append(string[i]);
        i+=1;
    i=0;
    while(i<len(list)-1):
        if(list[i]<list[i+1]):
            num-=1;
            del list[i];
            if(num==0):
                break;

            i-=1;
        i+=1;
    i=0;
    ans="";
    while(i<len(list)):
        ans+=list[i];
        i+=1;
    print(ans,end="");
def generateNum(NumList):
    i=0;
    while(i<len(NumList)):
        NumList.append(2*NumList[i]+1);
        NumList.append(4 * NumList[i] + 5);
        if(len(NumList)>1000):
            return NumList;
            break;
        i+=1;

try:
    inputList=input().split(" ");
    K=int(inputList[0]);
    num=int(inputList[1]);
except Exception as e:
    K = int(inputList[0]);
    num = int(inputList[2]);
model = sorted(generateNum([1]));
todoS="";

i=0;
while(i<K):
    todoS+=str(model[i]);
    i+=1;

print(todoS);
editNum(todoS,num);