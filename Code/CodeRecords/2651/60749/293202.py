n=int(input())
def convert(num):
    str1=""

    while(num>0):
        str1=str(num%2)+str1
        num=num//2
    if len(str1)%2==1:
        str1="0"+str1
    str2=""
    for i in range(0,len(str1)//2+2,2):
        if i<len(str1):

            str2+=str1[i+1]
            str2+=str1[i]

    res=0
    for h in range(0,len(str1)):
        res+=int(str2[h])*pow(2,len(str2)-1-h)
    return res
res=[]

for _ in range(n):
    t=int(input())
    res.append(convert(t))
for  m in res:
    print(m)