num=int(input());
count=0;
for i in range(10,num+1):
    string=str(i);
    for j in range(len(string)):
        if(string.count(string[j])>=2):
            count+=1;
            break;
print(count);