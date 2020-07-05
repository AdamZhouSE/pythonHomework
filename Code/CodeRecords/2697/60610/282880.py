num=input();
num=num.replace("[","")
num=num.replace("]","")
num=num.split(",")
for i in range(len(num)):
    if(num[i]=="null"):
        if(i%2==0):
            num[i]="-1";
        else:
            num[i]="100000";
num=list(map(int,num));
result=[0];
for i in range(len(num)-1):
    result.append(i//2+1);
count=0;

for i in range(1,len(result)):
    if(i%2==1):
        if(num[result[i]]<num[i]):
            count=1;
            break;
    else:
        if(num[result[i]]>num[i]):
            count=1;
            break;
if(count==1):
    print("false");
else:
    print("true");

