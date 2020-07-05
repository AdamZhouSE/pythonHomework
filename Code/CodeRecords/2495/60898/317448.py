class Larger(str):
    def __lt__(x,y):
        i=0
        if len(x)==len(y):
           for i in range(0,len(x)):
               if(x[i]!=y[i]):
                   return x[i]<y[i]
        else:
            return len(x)>len(y)


str=input().strip()
dic=eval(input())
dic=sorted(dic,key=Larger)
i=j=k=0
isFind=0
result=""
for i in range(len(dic)):
    j=k=0
    while (j<len(str))&(k<len(dic[i])):
        if str[j]==dic[i][k]:
            k+=1
        j+=1
    if k==len(dic[i]):
        isFind=1
        result=dic[i]
        break
print(result)