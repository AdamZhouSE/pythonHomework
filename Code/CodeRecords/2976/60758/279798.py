string=[]
de=input()
for i in range(0,6):
    string.append(input())
for i in range(0,len(string)):
    if de in string[i]:
        string[i]=string[i].replace(de,"")
for i in string:
    print(i)  