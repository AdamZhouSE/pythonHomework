string=input();
ins=int(string.split()[0]);
D=int(string.split()[1]);
result=[];
t=0;
for i in range(ins):
    string=input();
    num=int(string[2:]);
    if string[0]=="Q":
        print(max(result[len(result)-num:]));
        t=max(result[len(result)-num:]);
    else:
        result.append((t+num)%D);