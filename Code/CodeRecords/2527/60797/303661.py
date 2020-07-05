class Solution:
    def find(self, r, veganFriendly, maxPrice, maxDistance):
        res = []
        for i in range(len(r)):
            if r[i][2] >= veganFriendly and r[i][3] <= maxPrice and r[i][4] <= maxDistance:
                res.append(r[i][0:2])
        res = sorted(res, key=lambda x: x[0], reverse=True)
        res = sorted(res, key=lambda x: x[1], reverse=True)
        for i in range(len(res)):
            res[i] = res[i][0]
        return res


if __name__ == '__main__':
    data = input().strip('[]').split('],[')  # restaurants[i] = [idi, ratingi, veganFriendlyi, pricei, distancei]
    for i in range(len(data)):
        tmp = [int(a) for a in data[i].split(',')]
        data[i] = tmp
    veganFriendly = int(input())
    maxPrice = int(input())
    maxDistance = int(input())

    s = Solution()
    res = s.find(data, veganFriendly, maxPrice, maxDistance)
    print(res)
