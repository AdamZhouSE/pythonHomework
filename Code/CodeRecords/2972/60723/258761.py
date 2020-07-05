number=int(input())
for i in range(number):
    str1=input()
    str2=input()
    count=0
    for j in range(len(str1)):
        flag=False
        while count<len(str2):
            if str2[count]==str1[j]:
                count=count+1
                flag=True
                break
            count=count+1
        if j<len(str1)-1 and str1[j]!=str1[j+1]:
            if count==1 and str2[count]==str2[count-1]:
                flag=False
                break
            elif str2[count]==str2[count-1] and str2[count]==str2[count+1]:
                flag=False
                break
        elif j==len(str1)-1 and count<len(str2) and str2[count]==str2[count-1]:
            flag=False
            break
    if flag:
        print("Yes")
    else:
        print("No")