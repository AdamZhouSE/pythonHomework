x=int(input())
string=input()
for i in range(0,x):
    temp=list(input().split(" "))
    if temp[0]=="1":
        string=string+temp[1]
        print(string)
    if temp[0]=="2":
        string=string[int(temp[1]):int(temp[1])+int(temp[2])]
        print(string)
    if temp[0]=="3":
        string=string[0:int(temp[1])]+temp[2]+string[int(temp[1]):]
        print(string)
    if temp[0]=="4":
        print(string.find(temp[1]))