str1=input().split(' ')
n=int(str1[0])
m=int(str1[1])
num=[]
num.append(str(0))
boom=1
for i in range(n):
    num.append(str(0))
for i in range(m):
    str2=input().split(' ')
    if str2[0]=='1':
        for j in range(int(str2[1]),int(str2[2])+1):
            num[j]=num[j]+' '+str(boom)
        boom=boom+1
    elif str2[0]=='2':
        ans=[]
        count=0
        for j in range(int(str2[1]),int(str2[2])+1):
            list1=num[j].split(' ')
            for m in range(len(list1)):
                ans.append(list1[m])
        for i in range(len(ans)):
            for j in range(i+1,len(ans)):
                if(ans[i]==ans[j]):
                    ans[j]='0'
        for i in range(len(ans)):
            if(ans[i]!='0'):
                count=count+1
        print(count)
        
        