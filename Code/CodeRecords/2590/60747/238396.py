n=int(input())
string=[]
for i in range(n):
    string.append(input())
for i in range(n):
    if len(set(string[i]))%2==0:
        string[i]="SHE!"
    else:
        string[i]="HE!"
    print(string[i])