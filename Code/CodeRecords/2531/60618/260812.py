s=list(input())
news=set(s)
num=[]*len(news)
re=''
for i in range(0,len(news)):
    num.append(s.count(news[i]))
for i in range(0,len(num)):
    re+=max(num)*news[num.index(max(num))]
    num[num.index(max(num))]=-1
print(re)
    