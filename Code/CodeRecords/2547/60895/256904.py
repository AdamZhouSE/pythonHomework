t=int(input())
while t>0:
    t=t-1
    length=int(input())
    s=list(input())
    str=[]
    for item in s:
        if item!=' ':
            str.append(item)
    k=int(input())
    num=0
    for i in range(0,length-1):
        for j in range(i+1,length):
            if int(str[i])<int(str[j]):
                str[i],str[j]=str[j],str[i]
    re=[]
    re.append(str[0])
    re.append(str[1])  
    for m in range(2,length):
        if str[m-2]==str[m-1] and str[m-1]==str[m]:
            continue
        else:
            re.append(str[m])
    for i in range(0,(len(re)-1)):
        for j in range(i+1,len(re)):
            if k==int(re[i])-int(re[j]):
                num=num+1
                break
    print(num)                         
                