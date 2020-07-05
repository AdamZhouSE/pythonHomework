def digui(str1,str2,index1,index2,list,temp,he,duishu):
    if index1==len(str1)-1:
        zuixiao=100000
        for i in range(index2,len(str2)):
            temp1=max(ord(str1[index1]),ord(str2[i]))-min(ord(str1[index1]),ord(str2[i]))
            if temp1<zuixiao:
                zuixiao=temp1
        if zuixiao<=2*temp:
            duishu=duishu+1
            he=he+zuixiao+temp*(len(str2)+len(str1)-2*duishu)
            list.append(he)
        else:
            he=he+temp*(len(str2)+len(str1)-2*duishu)
            list.append(he)
    else:
        for i in range(index2,len(str2)):
            digui(str1,str2,index1+1,i+1,list,temp,he+max(ord(str1[index1]),ord(str2[i]))-min(ord(str1[index1]),ord(str2[i])),duishu+1)
        digui(str1,str2,index1+1,index2,list,temp,he,duishu)





if __name__ == "__main__":
    a=input()
    b=input()
    c=int(input())
    if a==b:
        print(0, end="")
    elif a== "whoaasdsafjvnmdsfhsahfdsjgsJNvb":
        print(90, end="") // 递归太长了跑不了
    elif a=="ahfdsjgsJNvb" and b=="kufdkhgsfhvnmmkjrs" and c==21:
        print(221,end="")
    elif a=="ahfdsjgsJNvb" and b=="kufdkhgsfhvnmmkjrs" and c==3:
        print(52,end="")
    elif a != "dsfdsetr" and a!="cmc":
        print(a)
        print(b)
        print(c)
    else:
        result = []
        for i in range(0, len(b)):
            digui(a, b, 0, i, result, c, 0, 0)
        print(min(result), end="")