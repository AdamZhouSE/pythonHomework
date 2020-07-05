
N=int(input())
articles=[]
for i in range(N):
    temp=input().split(' ')
    articles.append(temp[1:])
M=int(input())
to_search=[]
for i in range(M):
    to_search.append(input())


def sort(articles,to_search):
    num=[]
    cons=[]
    for k in to_search:
        temp=[]
        for i in range(len(articles)):
            if articles[i].count(k)!=0:
                temp.append(i+1)
        cons.append(temp)
    return cons

for i in sort(articles,to_search):
    st1r=''
    for k in i:
        st1r+=str(k)    
    print(' '.join(st1r),end=' ')
    print('')

