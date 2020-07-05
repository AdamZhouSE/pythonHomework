t=int(input())
for i in range(t):
    n=int(input())
    ans=[]
    str1=input()
    flag=0
    for i in range(len(str1)):
        if(str1[i])==',':
            flag=1
    if flag==1:
        list1=str1.split(',')
    else:
        list1=str1.split(' ')
    num=[]
    for i in range(len(list1)):
        if list1[i]!='':
            num.append(int(list1[i]))
    for i in range(len(num)):
        for j in range(len(num)):
            for k in range(len(num)):
                for m in range(len(num)):
                    if i!=j and i!=k and i!=m and j!=k and j!=m and k!=m:
                         if num[i]+num[j]==num[k]+num[m]:
                            ans.append(i)
                            ans.append(j)
                            ans.append(k)
                            ans.append(m)
    a_s=''
    if len(ans)<4:
        print('no pairs')
    else:
        a_s=str(ans[0])+' '+str(ans[1])+' '+str(ans[2])+' '+str(ans[3])
        print(a_s)