str1=input()
str2=input()
list=input().split()
zimu=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
res=[]
temp=[]
temp.append(str1)
res.append(temp)
finalres=[]
a=1
def xiangdneg(str1,str2):
    if len(str1) !=len(str2):
        return False
    else:
        for i in range(len(str1)):
            if str1[i]!=str2[i]:
                return False
        return True
numm=0
a=1
while numm==0:
    tempresu=[]
    for i in range(len(res)):
        str=res[i][-1]
        n=len(str)
        for j in range(n):
            for k in range(len(zimu)):
                strr=''
                strr=str[0:j] + zimu[k] + str[j + 1:len(str)]
                if strr in list and strr not in res[i]:
                    templist=[]
                    for m in res[i]:
                        templist.append(m)
                    templist.append(strr)
                    tempresu.append(templist)
    res=[]
    for m in tempresu:
        res.append(m)
    for i in res:
        if xiangdneg(i[-1],str2):
            finalres.append(i)
            numm=1
    if numm==1:
        break
    a+=1
    if a>len(list):
        break
if len(finalres)==0:
    print('[]')
else:
    print(finalres)