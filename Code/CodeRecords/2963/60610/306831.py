num=int(input());
mid=[];
for i in range(num-1):
    string=list(map(int,input().split()))
    mid.append(string);
fath=[[0,0] for i in range(num+1)];
for i in mid:
    fath[i[1]]=[i[0],i[2]];
count=0;
result=[];
for i in range(1,num+1):
    for j in range(i+1,num+1):
        if(i!=j):
            string="";
            string1="";
            string2="";
            string1count=[];
            string2count=[];
            k=i;
            l=j;
            while((fath[l][0]!=0)| (fath[k][0] != 0)):
                string1count.append(k);
                string1 = string1 + str(fath[k][1]);
                if(fath[k][0]!=0):
                    if(fath[k][0]==j):
                        string2="";
                        break;
                    if(fath[k][0] in string2count):
                        string2=string2[:string2count.index(fath[k][0])];
                        break;
                    k = fath[k][0];

                if(fath[l][0]!=0):
                    string2count.append(l)
                    string2 = string2 + str(fath[l][1]);
                    if (fath[l][0] == i):
                        string1 = "";
                        break;
                    if (fath[l][0] in string1count):
                        string1 = string1[:string1count.index(fath[l][0]) ];
                        break;
                    l = fath[l][0];
                if(fath[k][0]==fath[l][0]):
                    break;

            string=string1+string2[::-1];
            Rstring=string[::-1];
            if(string==Rstring):
                count+=1;
                result.append([i,j]);
print(count);