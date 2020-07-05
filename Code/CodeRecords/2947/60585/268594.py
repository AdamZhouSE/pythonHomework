n=eval(input())
string=input()
for _ in range(n):
    option=list(input().strip().split(' '))
    if option[0]=='1':
        string+=option[1]
        print(string)
    elif option[0]=='2':
        a=int(option[1])
        b=int(option[2])
        string=string[a:a+b]
        print(string)
    elif option[0]=='3':
        a=int(option[1])
        temp=string[:a]
        temp+=option[2]
        string=temp+string[a:]
        print(string)
    elif option[0]=='4':
        print(string.find(option[1]))