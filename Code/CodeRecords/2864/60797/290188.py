class Solution:
    def find(self, n, data):
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
        while i < len(k) - 1: # 到倒数第二个
            if k[i] == k[i+1] + 1:
                if dd[i] * k[i] > dd[i + 1] * k[i + 1]:
                    re += dd[i] * k[i]
                    i += 1
                    if i == len(k) - 2:
                        re += dd[i + 1] * k[i + 1]
                        break
                else:
                    re += dd[i + 1] * k[i + 1]
                    # re += dd[i] * k[i]
                    i += 1
                i += 1
            else:
                re += dd[i] * k[i]
                i+=1
        return re


if __name__ == '__main__':
    n = int(input())
    data = [int(a) for a in input().split(', ')]
    s = Solution()
    re = s.find(n, data)
    print(re)

# 29, 15, 54, 67, 65, 74, 53, 25, 74, 29, 11, 55, 2, 15, 2, 1, 12, 95, 16, 81, 51, 40, 28, 54, 27, 80, 33, 10, 39, 45, 25, 99, 64, 22
