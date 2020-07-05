import functools
import _functools
def tcmp(a: list,b: list):
    if int(a[1]) > int(b[1]):
        return 1
    elif int(a[1]) < int(b[1]):
        return -1
    else:
        if int(a[0]) > int(b[0]):
            return 1
        else:
            return -1
#restaurants[i] = [idi, ratingi, veganFriendlyi, pricei, distancei]
def func(l: list,vegan: int, price: int, distance: int) -> list:
    answerList, answerListRes = [], []
    for i in l:
        if (vegan==1 and i[2]==0) or (price < int(i[3])) or (distance < int(i[4])):
            continue
        else:
            answerList.append(i)
    nums = sorted(answerList, key=_functools.cmp_to_key(tcmp), reverse=True)
    for i in nums:
        answerListRes.append(i[0])
    return answerListRes

n = "l = "+ input()
exec(n)
vegan = int(input())
price = int(input())
distance = int(input())
print(func(l,vegan,price,distance))