def substring(str1):
    lenn=len(str1)
    n=2**lenn
    list1=[]
    for i in range(0,n):
        str2=bin(i)[2:]
        while len(str2)<lenn:
            str2="0"+str2
        str3=""
        for j in range(0,lenn):
            if str2[j]=='1':
                str3+=str1[j]
        list1.append(str3)
    return list1

def isTrue(str1):
    if (not 'a' in str1) or (not 'b' in str1) or (not 'c' in str1):
        return False
    else:
        aflag=1
        bflag=1
        cflag=1
        for i in str1:
            if i!='a':
                aflag=0
            if i=='c':
                bflag=0
            if i=='a' and aflag==0:
                return False
            if i=='b' and bflag==0:
                return False
        return True
        
n=int(input())
for i in range(0,n):
    list1=substring(input())
    count=0
    for j in list1:
        if isTrue(j):
            count+=1
    print(count)