class Solution:
    def find(self, n, data):
        f = dict()
        for i in range(n):

            f[data[i]] = f.get(data[i], 0) + 1

        sorted_key_list = sorted(f, key=lambda x: f[x], reverse=True)
        sorted_dict = map(lambda x: {x: f[x]}, sorted_key_list)

        f = list(sorted_dict)
        re = []
        for item in f:
            k = list(item.keys())[0]
            re.append([k, item[k]])
        for i in range(len(re)):
            ptr = i+1
            arr = []
            arr.append(re[i][0])
            while ptr<len(re) and re[ptr][1]==re[i][1]:
                arr.append(re[ptr][0])
                ptr += 1
            left = i
            right = ptr -1
            dis = right - left +1
            for i in range(left,right+1):
                re[i][0] = arr[dis - i - 1]
        for item in re:
            for i in range(item[1]):
                print(item[0],end=' ')
        print()
        return


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        data = [int(a) for a in input().split()]
        s = Solution()
        s.find(n, data)

