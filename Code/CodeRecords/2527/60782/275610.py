"""
题目描述
    给你一个餐馆信息数组 restaurants，其中 restaurants[i] = [idi, ratingi, veganFriendlyi, pricei, distancei]。你必须使用以下三个过滤器来过滤这些餐馆信息。
        其中素食者友好过滤器 veganFriendly 的值可以为 true 或者 false，
    如果为 true 就意味着你应该只包括 veganFriendlyi 为 true 的餐馆，为 false 则意味着可以包括任何餐馆。
        此外，我们还有最大价格 maxPrice 和最大距离 maxDistance 两个过滤器，
    它们分别考虑餐厅的价格因素和距离因素的最大值。

    过滤后返回餐馆的 id，按照 rating 从高到低排序。
    如果 rating 相同，那么按 id 从高到低排序。
    简单起见， veganFriendlyi 和 veganFriendly 为 true 时取值为 1，为 false 时，取值为 0 。
        1 <= restaurants.length <= 10^4
        restaurants[i].length == 5
        1 <= idi, ratingi, pricei, distancei <= 10^5
        1 <= maxPrice, maxDistance <= 10^5
    veganFriendlyi 和 veganFriendly 的值为 0 或 1 。
    所有 idi 各不相同。
"""
"""
输入描述
    一个餐馆信息数组 restaurants，其中  restaurants[i] = [idi, ratingi, veganFriendlyi, pricei, distancei]。
    素食者友好过滤器 veganFriendly，以及最大价格 maxPrice 和最大距离 maxDistance 两个过滤器。
"""
"""
输出描述
    返回餐馆的 id，按照 rating 从高到低排序。
    如果 rating 相同，那么按 id 从高到低排序。
"""
restaurants = eval(input())
vegan_friendly_i = int(input())
max_price = int(input())
max_distance = int(input())
if not restaurants:
    return []
res = []
for i, rating, vF, mP, mD in restaurants:
    if not vegan_friendly_i or (vF and vegan_friendly_i):
        if mP <= max_price and mD <= max_distance:
            res.append([i, rating])
return [i for i, rating in sorted(res, key = lambda x:(x[1], x[0]), reverse = True)]

