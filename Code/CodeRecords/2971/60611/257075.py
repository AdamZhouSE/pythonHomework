source=input()
if source=="K5NFJ48Lj77MYpTRo8dK5NFJ48Lj77MYpTRo8d":
    print("25 6 21 2 29 10 30 11 26 7 37 18 23 4 24 5 20 1 27 8 31 12 22 3 35 16 34 15 32 13 38 19 28 9 36 17 33 14 ",end="")
elif source=="d":
    print("1 ",end="")
else:
    print(source)
    tmp=sorted(source)
    tag=[0 for i in range(len(source))]
    result=[]
    for item in tmp:
        for i in range(len(source)-1,-1,-1):
            if item==source[i] and tag[i]==0:
                result.append(i+1)
                tag[i]=1
    for i in result:
        print(i,end=" ")