class Solution:
    def find(self, n, data):
        if n == 1:
            return data[0]
        re = 0
        d = dict()
        for i in range(n):
            d[data[i]] = data.count(data[i])

        # 这两行可以好好学习一下！！！
        sorted_key_list = sorted(d, reverse=True)  # key从大到小
        sorted_dict = sorted(d.items(), key=lambda x: x[0], reverse=True)

        k = sorted_key_list
        dd = []
        for item in sorted_dict:
            dd.append(item[1])
        i = 0
        while i < len(k):
            if k[i] == k[i+1] + 1: # 下一个不能要了
                if dd[i] * k[i] > dd[i + 1] * k[i + 1]:
                    re += dd[i] * k[i]
                    i += 1
                    if i == len(k) - 1:
                        break
                    if i == len(k) - 2:
                        re += dd[i + 1] * k[i + 1]
                        break
                else:
                    re += dd[i + 1] * k[i + 1]
                    i += 1
                    if i == len(k) - 1:
                        break
                    if k[i] == k[i+1]+1:
                        i += 1
                i += 1
            else: # 下一个还能要
                re += dd[i] * k[i]
                i += 1
                if i == len(k) - 1:
                    re += dd[i] * k[i]
                    break
        return re


if __name__ == '__main__':
    n = int(input())
    data = [int(a) for a in input().split()]
    s = Solution()
    re = s.find(n, data)
    print(re)



