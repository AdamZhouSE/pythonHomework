str1=input()
str1=str1.strip("[")
str1=str1.strip("]")
str1=str1.split(",")

def minius(time1,time2):
    time1=time1.strip('"')
    time2=time2.strip('"')
    time1=time1.split(":")
    time2=time2.split(":")
    num1=int(time1[0])*60+int(time1[1])
    num2=int(time2[0])*60+int(time2[1])
    minius=abs(num1-num2)
    if minius>24*60-minius:
        return 24*60-minius
    else:
        return minius
res=[]
for i in range(0,len(str1)-1):
    for j in range(i+1,len(str1)):
        res.append(minius(str1[i],str1[j]))
res=sorted(res)
print(res[0])
