num=int(input())
res=list()
for k in range(num):
    str1=input().split(" ")
    str2=input().split(" ")
    str3=input().split(" ")

    judge2=str2.copy()
    judge2.sort()
    judge3=str3.copy()
    judge3.sort()
    if judge2!=judge3:
        res.append("NO")
    else:
        flag=False
        i=1
        length=len(str3)
        while flag!=True and i<length-2:
            if "".join(str3[0:i]) not in "".join(str2):
                i=i+1
                continue
            j=i+1
            while flag!=True and j<length:
                if ("".join(str3[i:j]) in "".join(str2)) and ("".join(str3[j:]) in "".join(str2)):
                    if(str3[0:i]+str3[j:]+str3[i:j]==str2):
                        flag = True
                        res.append("YES")
                        res.append("1 "+str(i))
                        res.append(str(j+1)+" "+str(len(str3)))
                        res.append(str(i+1)+" "+str(j))
                    elif(str3[i:j]+str3[0:i]+str3[j:]==str2):
                        flag = True
                        res.append("YES")
                        res.append(str(i+1)+" "+str(j))
                        res.append("1 "+str(i))
                        res.append(str(j+1)+" "+str(len(str3)))
                    elif (str3[i:j] + str3[j:]+ str3[0:i] == str2):
                        flag = True
                        res.append("YES")
                        res.append(str(i+1)+" "+str(j))
                        res.append(str(j+1)+" "+str(len(str3)))
                        res.append("1 "+str(i))
                    elif (str3[j:] + str3[0:i] + str3[i:j]== str2):
                        flag = True
                        res.append("YES")
                        res.append(str(j+1)+" "+str(len(str3)))
                        res.append("1 "+str(i))
                        res.append(str(i+1)+" "+str(j))
                    elif (str3[j:] + str3[i:j] + str3[0:i] == str2):
                        flag = True
                        res.append("YES")
                        res.append(str(j+1)+" "+str(len(str3)))
                        res.append(str(i+1)+" "+str(j))
                        res.append("1 "+str(i+1))
                j=j+1
            i=i+1
        if flag==False:
            res.append("NO")
for i in res:
    print(i)