n=int(input())
string=[]
for i in range(n):
    string.append(int(input()))
    if string[i]%2==0:
        string[i]="Player B"
    else:
        string[i]="Player A"
for i in range(n):
    print(string[i])
