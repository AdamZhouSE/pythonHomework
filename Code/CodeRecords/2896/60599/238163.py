s1=input()
s2=input()
s2="".join(s2.split(' '))
for i in s2:
    flag = 0
    for z in range(len(s1)):
        if s1[z]==i :
            s1=s1[:z]+'1'+s1[z+1:]
            flag=1
            break
    if(flag==0):
        print('NO')
        exit()
print('YES')
