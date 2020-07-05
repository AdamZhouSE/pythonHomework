n=int(input())
string=[]
for i in range(n):
    string.append(int(input()))
    if string[i]%2==0:
        string[i]="PlayerB"
    else:
        string[i]="PlayerA"
for i in range(n):
    print(string[i])
