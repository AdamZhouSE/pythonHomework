def change(string,a,b):
    temp=""
    if(a>b):
        c=a
        a=b
        b=c
    if(a==b):return string
    if(a==0 and b==len(string)-1):
        if(string[a]>string[b]):
            temp=string[b]+string[1:-1]+string[a]
    elif(a==0):
        if (string[a] > string[b]):
            temp=string[b]+string[1:b]+string[0]+string[b+1:]
    elif(b==len(string)-1):
        if (string[a] > string[b]):
            temp=string[:a]+string[b]+string[a+1:b]+string[a]
    else:
        if(string[a]>string[b]):
            temp=string[:a]+string[b]+string[a+1:b]+string[a]+string[b+1:]
    return temp

def isnotDict(string,a,b):
    if(string[a]<string[b]):return False
    return True

string=input()
inp=input()
pairs=inp[2:-2].split("],[")
for i in range(len(pairs)):
    pairs[i]=pairs[i].split(",")
for i in range(len(pairs)):
    for j in range(2):
        pairs[i][j]=int(pairs[i][j])

while(True):
    st=True
    for i in range(len(pairs)):
        if(isnotDict(string,pairs[i][0],pairs[i][1])):
            string=change(string,pairs[i][0],pairs[i][1])
    for i in range(len(pairs)):
        if(isnotDict(string,pairs[i][0],pairs[i][1])):
            st=False
    if(st==True):
        break

print(string)

