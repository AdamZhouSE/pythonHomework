class Solution:
    def find(self, n, data):
        re = 0
        d = dict()
        for i in range(n):
            d[data[i]] = data.count(data[i])

        # 这两行可以好好学习一下！！！
        sorted_key_list = sorted(d, reverse=True)  # key从大到小
        sorted_dict = map(lambda x: {x: d[x]}, sorted_key_list)

        k = sorted_key_list
        d = sorted_dict
        for i in range(len(k) - 1):
            
            if d[i] * k[i] > d[i + 1] * k * [i + 1]:
                re += d[i] * k[i]
                if i==len(k)-2:
                    re += d[i + 1] * k * [i + 1]
                    break
            else:
                re += d[i + 1] * k * [i + 1]
                re += d[i] * k[i]
                i+=1
        return re


if __name__ == '__main__':
    n = int(input())
    data = [int(a) for a in input().split()]
    s = Solution()
    re = s.find(n, data)
    print(re)
