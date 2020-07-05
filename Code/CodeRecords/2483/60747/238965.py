n=int(input())
result=[0for i in range(n)]

for i in range(n):
    string1=input()
    string=input()
    string2=[]
    for m in string:
        string2.append(m)
    num=[]
    for p in range(len(string2)):
        if string1.find(string2[p])!=-1:
            num.append(string1.find(string2[p]))
    if len(num)==0:
        result[i]="$"
    else:
        num.sort()
        result[i]=string1[num[0]]
for i in range (n):
    print(result[i])