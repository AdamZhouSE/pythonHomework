list1=['a','e','i','o','u','A','E','I','O','U']
n=int(input())
for i in range(0,n):
    list2=[]
    str1=input()
    len1=len(str1)
    for j in range(1,2**len1):
        str2=bin(j)[2:]
        while len(str2)<len1:
            str2="0"+str2
        str3=""
        for k in range(0,len1):
            if str2[k]=='1':
                str3+=str1[k]
        if str3[0] in list1 and (not str3[len(str3)-1] in list1) and (not str3 in list2):
            list2.append(str3)
    if list2==[]:
        print(-1)
    else:
        list2.sort()
        str4=''
        for j in list2:
            str4+=j
            str4+=' '
        print(str4[:-1])    