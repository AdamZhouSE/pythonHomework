"""
给你一个餐馆信息数组 restaurants，其中 restaurants[i] = [idi, ratingi, veganFriendlyi, pricei, distancei]
你必须使用以下三个过滤器来过滤这些餐馆信息
其中素食者友好过滤器 veganFriendly 的值可以为 true 或者 false
如果为 true 就意味着你应该只包括 veganFriendlyi 为 true 的餐馆，为 false 则意味着可以包括任何餐馆
此外，我们还有最大价格 maxPrice 和最大距离 maxDistance 两个过滤器，它们分别考虑餐厅的价格因素和距离因素的最大值
过滤后返回餐馆的 id，按照 rating 从高到低排序
如果 rating 相同，那么按 id 从高到低排序
简单起见， veganFriendlyi 和 veganFriendly 为 true 时取值为 1，为 false 时，取值为 0
"""

restaurants=eval(str(input()))
veganFriendly=int(input())
maxPrice=int(input())
maxDistance=int(input())

restaurants.reverse()
i=0
while(i<len(restaurants)):
    if((restaurants[i][2]==0 and veganFriendly==1) or restaurants[i][3]>maxPrice or restaurants[i][4]>maxDistance):
        del restaurants[i]
    else:
        i+=1

ratingi=[]
for i in range(len(restaurants)):
    ratingi.append(restaurants[i][1])

result=[]
while(sum(ratingi)!=0):
    result.append(restaurants[ratingi.index(max(ratingi))][0])
    ratingi[ratingi.index(max(ratingi))]=0

print(result)