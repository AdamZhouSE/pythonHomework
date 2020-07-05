#import itertools;
YES = 'YES'
NO = 'NO'
len1,len2 = map(int,input().split());
#print(len1,len2);
#print(type(len1));
k,m = map(int,input().split());
#print(k,m);
lista = input().split(" ");
lista = [int(lista[i]) for i in range(len(lista))];
#print(lista);
listb = input().split(" ");
listb = [int(listb[i]) for i in range(len(listb))];
#print(listb)
result = 0;
for b in listb:
    temp = 0;
    for a in lista:
        if(b>a):temp=temp+1;
        #print(temp)
    if (temp>=k):result=result+1;
if result>=m:
    print(YES)
else:
    print(NO)
            