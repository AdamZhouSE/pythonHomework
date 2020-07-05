class Solution:
    def find(self, d):
        tmp = [d[0]]
        count =1
        for i in range(len(d)):
            if d[i]>max(tmp):
                tmp=[d[i]]
                count+=1
            else:
                tmp.append(d[i])
        return count


if __name__ == '__main__':
    data = [int(a) for a in input().strip('[]').split(',')]
    s = Solution()
    res = s.find(data)
    print(res)

