string=[]
de=input()
for i in range(0,6):
    string.append(input())
for i in range(0,len(string)):
    string[i]=string[i].replace(' ',"")
    if de in string[i]:
        string[i]=string[i].replace(de,"")
    if de.upper() in string[i]:
        string[i]=string[i].replace(de.upper(),"")
for i in string:
    print(i)      