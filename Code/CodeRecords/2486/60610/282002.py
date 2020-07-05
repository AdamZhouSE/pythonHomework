num=int(input());
for i in range(num):
    string=input();
    while("[" in string):
        left=string.rfind("[");
        right=string.find("]");
        string=string.replace(string[left-1:right+1],string[left+1:right]*int(string[left-1]));
    print(string);
