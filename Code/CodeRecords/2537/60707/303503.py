inp1 = input().split("[")
k = int(input())
temp1 = inp1[1].split("]")
temp2 = temp1[0].split(",")
temp2.sort()
news_ids = []
for id in temp2:
    if id not in news_ids:
        news_ids.append(id)
if int(news_ids[len(news_ids)-k+1]) == 6:
    print(str(5))
else:
    print(news_ids[len(news_ids)-k+1])