str1=input().split(' ')
L=int(str1[0])
T=int(str1[1])
O=int(str1[2])
color=[]
for i in range(L+1):
    list1=[1]
    color.append(list1)
for i in range(O):
    str2=input().split(' ')
    if str2[0]=='C':
        for j in range(int(str2[1]),int(str2[2])+1):
            color[j].append(int(str2[3]))
    elif str2[0]=='P':
        ans=[]
        for j in range(int(str2[1]),int(str2[2])+1):
            for s in range(len(color[j])):
                ans.append(color[j][s])
        for m in range(len(ans)):
            for n in range(m+1,len(ans)):
                if ans[m]==ans[n]:
                    ans[n]=0
        count=0
        for i in range(len(ans)):
            if ans[i]!=0:
                count=count+1
        if count>(int(str2[2])-int(str2[1]))+1:
            count=(int(str2[2])-int(str2[1]))+1
        print(count)