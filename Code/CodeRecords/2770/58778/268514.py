n=int(input())
def sec(lis):
    return lis[1]
for i in range(n):
    m=int(input())
    str1=input()
    str2=input()
    numlist1=[]
    numlist2=[]
    for j in str1.split( ):
        numlist1.append(int(j))
    for j in str2.split( ):
        numlist2.append(int(j))
    temp=[]
    for j in range(len(numlist1)):
        c=[]
        c.append(numlist1[j])
        c.append(numlist2[j])
        temp.append(c)
    temp.sort(key=sec)
    re=[]
    c=[]
    for i in range(len(temp)):
        if(i==0):
            re.append(numlist2.index(temp[i][1]))
            c.append(temp[i][1])
        else:
            if(temp[i][0]>c[-1]):
                re.append(numlist2.index(temp[i][1]))
                c.append(temp[i][1])
    for i in range(len(re)):
        print(re[i]+1,'',end='')
        
    print('')
