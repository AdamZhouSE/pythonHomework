class Solution:
    def find(self, data, n):
        if len(data)==0:
            return 0
        p = []
        count = 0
        while True:
            q = []
            for i in range(len(data)):
                tmp = data[i]
                if len(p)!=0:
                    for item in p:
                        tmp += item
                        if int(tmp) <= n:
                            count += 1
                            q.append(tmp)
                            tmp = tmp[:len(tmp)-1]
                        else:
                            return count
                else:
                    if int(tmp) <= n:
                        count += 1
                        q.append(tmp)
                    else:
                        return count
            p = q

if __name__ == '__main__':
    data = input().split(',')
    n = int(input())
    s = Solution()
    re = s.find(data, n)
    print(re)
