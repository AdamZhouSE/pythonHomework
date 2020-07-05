string=input().split();
P_num=int(string[0]);
Q_num=int(string[1]);
result=[[0,0,0,0,0] for i in range(Q_num)];
for i in range(P_num):
    string=input();
    for j in range(Q_num):
        if string[j]=="A":
            result[j][0]+=1;
        elif string[j]=="B":
            result[j][1]+=1;
        elif string[j] == "C":
            result[j][2] += 1;
        elif string[j] == "D":
            result[j][3] += 1;
        else:
            result[j][4] += 1;
sum=0;
string=list(map(int,input().split()))
for i in range(len(result)):
    sum=sum+max(result[i])*string[i]
print(sum);