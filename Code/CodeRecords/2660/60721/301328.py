n=int(input())
text=[]
for o in range(0,n):
    s=input().split(" ")
    if(s[0]=="T"):
        text.append(s[1])
    elif(s[0]=="Q"):
        print(text[int(s[1])-1])
    else:
        for i in range(0,int(s[1])):
            text.pop(len(text)-1)