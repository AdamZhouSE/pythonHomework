testnum=int(input())
for i in range(testnum):
    string=input()
    num1=int(string)
    string=[i for i in string]
    for i in range(len(string)):
        if(string[i]=="6"):
            string[i]="9"
    string="".join(string)
    num2=int(string)
    print(num2-num1)