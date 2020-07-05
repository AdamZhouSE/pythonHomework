s1=input()
s2=input()
for i in range(len(s2)):
    if s2[i]!=' ':
        index=s1.find(s2[i])
        if index!=-1:
            s1=s1[:index]+s1[index+1:]
        else:
            print('NO',end='')
            exit()
print('YES',end='')
    

