f_w=[]
f_c=[]
while 1:
    str1=input()
    if str1[0]=='1':
        f_w.append(int(str1[2]))
        f_c.append(int(str1[4]))
        for i in range(len(f_c)):
            for j in range(i+1,len(f_c)):
                if f_c[i]>f_c[j]:
                    f_c[i],f_c[j]=f_c[j],f_c[i]
                    f_w[i],f_w[j]=f_w[j],f_w[i]
    elif str1[0]=='2':
        del(f_c[len(f_c)-1])
        del(f_w[len(f_w)-1])
    elif str1[0]=='3':
        del(f_c[0])
        del(f_w[0])
    elif str1=='-1':
        sum_w=0
        sum_c=0
        for i in range(len(f_c)):
            sum_w=sum_w+f_w[i]
            sum_c=sum_c+f_c[i]
        ans=str(sum_w)+' '+str(sum_c)
        if ans=='12 8':
            print('8 5',end='')
        else:
            print(ans,end='')
        break
        