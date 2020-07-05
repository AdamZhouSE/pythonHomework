string=input()
s=sorted(eval(input()))
count=0;
while(count==0):
    cout=0
    for i in s:
        for j in s:
            if(i!=j):
                if(i[0]==j[0]):
                    if([min(i[1],j[1]),max(i[1],j[1])] not in s):
                        s.append([min(i[1],j[1]),max(i[1],j[1])]);
                    else:
                        cout+=1;
                elif(i[1]==j[1]):
                    if ([min(i[0], j[0]), max(i[0], j[0])] not in s):
                        s.append([min(i[0], j[0]), max(i[0], j[0])]);
                    else:
                        cout+=1;
                else:
                    cout+=1;
            else:
                cout+=1;
    if(cout==pow(len(s),2)):
        count=1;
count=0;
while(count==0):
    cout=0;
    for i in s:
        if(string[i[0]]>string[i[1]]):
            c=string[i[0]]
            string=string[:i[0]]+string[i[1]]+string[i[0]+1:];
            string = string[:i[1]] +c+ string[i[1] + 1:];
        else:
            cout+=1;
    if(cout==len(s)):
        count=1;
print(string)