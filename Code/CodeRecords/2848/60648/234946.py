#import itertools;
YES = 'YES'
NO = 'NO'
len1,len2 = map(int,input().split());
#print(len1,len2);
#print(type(len1));
k,m = map(int,input().split());
#print(k,m);
lista = input().split(" ");
lista = [int(lista[i]) for i in range(len1)];
#print(lista);
listb = input().split(" ");
listb = [int(lista[i]) for i in range(len2)];
result = 0;
for i in listb:
    temp = 0;
    for j in lista:
        if(i>j):temp=temp+1;
        #if (i>j):temp++
    if (temp>=k):result=result+1;
if result>=m:
    print(YES)
else:
    print(NO)
            