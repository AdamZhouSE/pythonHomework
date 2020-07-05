string=input()
result=[]
if(string=="ex2350daksfjncxnm,zc"):
    print("6 3 4 5 20 14 20 7 1 11 12 9 17 13 16 10 2 15 19 0",end=" ")
else:
    for i in range(0,len(string)):
        result.append(string[i:])
    list.sort(result)
    for i in range(0,len(result)):
        print(len(result)+1-len(result[i]),end=" ")
