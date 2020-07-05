n=int(input());
listSTR = input().split();
listNUM =[];
num=0;
for i in listSTR:
    listNUM.append(int(i));
a,b=map(int,input().split());
offset = b-a;
for i in range(a-1,b-1):
    num+=listNUM[i];
print(num);