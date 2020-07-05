def equals(str1,str2):
    for i in range(len(str1)):
        if(str1[i]==str2[i] or str1[i]=='*' or str2[i]=='*'):pass
        else:return False
    return True
input()
str1 = input()
str2 = input()
times=0
elist = []
for i in range(len(str2)-len(str1)+1):
    #print(str1,str2[i:i+len(str1)])
    if(equals(str1,str2[i:i+len(str1)])):
        times+=1
        elist.append(i+1)
print(times)
print("".join( [str(elist[i])+' ' for i in range(len(elist))]))