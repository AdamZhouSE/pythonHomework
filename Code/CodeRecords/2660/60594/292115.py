n=int(input())
s=""
for i in range(n):
    row=input().split()
    if row[0]=='T':
        s=s+row[1]
    elif row[0]=='U':
        n=int(row[1])
        s=s[:len(s)-n]
    elif row[0]=='Q':
        n = int(row[1])
        print(s[n-1])