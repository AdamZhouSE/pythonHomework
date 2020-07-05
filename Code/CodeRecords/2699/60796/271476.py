N=int(input())
string=[]
result=[]
for i in range(N):
    s=input()
    string.append(s.replace(" ",''))
print(string)
for i in range(N):
    ls=[]#表明一对必须要排前面的字母
    can=0
    j=0
    str1=string[i]
    #print("下面到：",str1)
    while j==i:
        j=j+1
    #现在string[j]是第一个和string[i]不同的字符串
    str2=string[j]
    k=0
    while str1[k]==str2[k]:
        k=k+1
        if k==len(str1) or k==len(str2):
            break
    #第一种情况：有不同的字母——在ls中添加这一对
    if k<len(str1) and k<len(str2):
        ls.append([str1[k],str2[k]])
        #print("现在的k", k, "len(str1)", len(str1), "len(str2)", len(str2))
        can=1
    else:#第二种情况：字符串2比字符串1短而且所有字符都相同，则字符串2肯定要排前面
        if len(str1)>len(str2):
            #print("现在的k",k,"len(str1)",len(str1),"len(str2)",len(str2))
            continue
        else:#第三种情况：字符串2比字符串1长且所有字符都相同，则字符串1肯定要排前面
            can=1

    j=j+1
    while j<len(string):
        if j!=i:
            str2=string[j]
            k=0
            while str1[k]==str2[k]:
                k=k+1
                if k==len(str1) or k==len(str2):
                    break
            #第一种情况——有不同的字母
            if k<len(str1) and k<len(str2):
                a=0
                while a<len(ls):
                    if ls[a][0]==str2[k] and ls[a][1]==str1[k]:
                        break
                    else:
                        a=a+1
                if a==len(ls):#str1可以排在str2前面，并且在ls里添加这一对
                    ls.append([str1[k],str2[k]])
                    can=can+1


            else:
                #第二种情况——字符串2不比1短
                if len(str1)<=len(str2):
                    can=can+1

        j=j+1
        #print(ls)
    if can==N-1:
        result.append(str1)
    #print("str1的can:",can)
print(len(result))
for i in range(len(result)):
    print(result[i])




