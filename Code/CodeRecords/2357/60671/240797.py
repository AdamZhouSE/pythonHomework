time=int(input())
while(time>0):
    str1=input()
    len1=int(str1[0])
    len2=int(str1[2])
    sum=int(str1[4])
    str01=input()
    list1=str01.split()
    listnum1=[]
    for x in list1:
        listnum1.append(int(x))
    str02=input()
    list2=str02.split()
    listnum2=[]
    for x in list2:
        listnum2.append(int(x))
    answer=[]
    for i in range(len1):
        for j in range(len2):
            if(listnum1[i]+listnum2[j]==sum):
                temp=[listnum1[i],listnum2[j]]
                answer.append(temp)
    lena=len(answer)
    for i in range(lena):
        print(*answer[i])
    time-=1