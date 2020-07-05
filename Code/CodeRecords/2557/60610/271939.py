num=int(input());
for i in range(num):
    string=input();
    for j in range(len(string)-1):
        if string[j]==string[j+1]:
            string=string[:j]+" "+string[j+1:];
    print("".join(string.split()))