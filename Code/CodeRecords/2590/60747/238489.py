n=int(input())
string=[]
count=0
for i in range(n):
    string.append(input())
for i in range(n):
    count = 0
    if "a" in set(string[i]):
        count=count+1
    if "e" in set(string[i]):
        count=count+1
    if "i" in set(string[i]):
        count = count + 1
    if "o" in set(string[i]):
        count = count + 1
    if "u" in set(string[i]):
        count = count + 1
    if (len(set(string[i]))-count)%2==0:
        string[i]="SHE!"
    else:
        string[i]="HE!"
    print(string[i])