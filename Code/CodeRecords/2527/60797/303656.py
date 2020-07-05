class Solution:
    def find(self, r, veganFriendly, maxPrice, maxDistance):
        res = []
        for i in range(len(r)):
            if r[2]==veganFriendly and r[3]<=maxPrice and r[4]<=maxDistance:
                res.append(r[0:2])
        res = sorted(res, key=lambda x:x[0],reverse=True)
        res = sorted(res,key=lambda x:x[0],reverse= True)



        return res


if __name__ == '__main__':
    data = input().strip('[]').split('],[') # restaurants[i] = [idi, ratingi, veganFriendlyi, pricei, distancei]
    for i in range(len(data)):
        tmp = [int(a) for a in data[i].split(',')]
        data[i] = tmp
    veganFriendly = int(input())
    maxPrice = int(input())
    maxDistance =int(input())

    s = Solution()
    res = s.find(data, veganFriendly, maxPrice, maxDistance)
    print(res)
