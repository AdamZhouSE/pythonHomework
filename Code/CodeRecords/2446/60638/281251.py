n=int(input())
letters=[]
for x in range(0,n):
    letters.append(input().split(" ")[1:])
m=int(input())
for x in range(0,m):
    letter=input()
    res=[]
    for i in range(0,len(letters)):
        if letters[i].__contains__(letter):
            res.append(i+1)
    if len(res)==0:
        print(" ")
    else:
        for i in range(0,len(res)-1):
            print(res[i],end=" ")
        print(res[-1],"")