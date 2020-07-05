class Solution:
    def find(self, d):
        totalof1 = d.count(1)
        if totalof1%3!=0:
            return [-1,-1]
        partof1 = totalof1 // 3
        count = 0
        re = []
        newbeg = []
        for i in range(len(d)):
            if d[i]==1:
                if count == 0:
                    newbeg.append(i)
                count += 1
                if count==partof1:
                    re.append(i)
                    count = 0
        endof0 = len(d)-1-re[2]
        if re[0]+endof0< newbeg[1] and re[1]+endof0<newbeg[2]:
            return [re[0]+endof0,re[1]+endof0+1]
        return [-1,-1]

if __name__ == '__main__':
    data = [int(a) for a in input().split(',')]
    s = Solution()
    re = s.find(data)
    print(re)