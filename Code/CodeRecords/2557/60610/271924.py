num=int(input());
for i in range(num):
    string=input();
    for j in string:
        if string.count(j)>=2:
            string=string.replace(j,"",1);
    print(string)