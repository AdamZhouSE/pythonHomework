s=input().split(" ")
n=int(s[0])
m=int(s[1])
house=[0for j in range(n)]
index=[]
result=[]
for i in range(m):
    count=0
    news=input()
    if len(news)!=1:
        news=news.split(" ")
    if news[0]=="D":
        house[int(news[1])-1]=1
        index.append(int(news[1])-1)
    elif news[0]=="R":
        if len(index)==0: continue
        else:
            house[index[len(index)-1]]=0
            del index[len(index)-1]
    else:
        p=int(news[1])-1
        if house[p]==1:
            result.append(count)
        else:
            while p>0:
                if house[p]==0:
                    count+=1
                else :break
                p-=1
            p=int(news[1])-1
            while p<n-1:
                if house[p+1]==0:
                    count+=1
                else : break
                p+=1
            result.append(count)
for h in range(len(result)):
    print(result[h])