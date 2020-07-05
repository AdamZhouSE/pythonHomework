testnum=int(input())
for i in range(testnum):
    string1=input()
    string2=input()
    anslist=[]
    for m in range(len(string1)):
        if(string1[m] not in string2):
            if(string1[m] not in anslist):
                anslist.append(string1[m])
    for m in range(len(string2)):
        if(string2[m] not in string1):
            if(string2[m] not in anslist):
                anslist.append(string2[m])
    anslist.sort()
    ans="".join(anslist)
    print(ans)
    print()