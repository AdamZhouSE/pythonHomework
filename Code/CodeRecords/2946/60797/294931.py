class Solution:
    def find(self, data):
        if len(data) == 1:
            if data[0]==1:
                return 0
            else:
                return  1
        re = 0
        pre = data[0]
        for i in range(1, len(data)):
            if data[i]==pre:
                continue
            else:
                re +=1
                pre = data[i]
        if data[len(data)-1]==0:
            re +=1
        return re


if __name__ == '__main__':
    s = input()
    data =[]
    for i in range(len(s)):
        data.append(eval(s[i]))
    s = Solution()
    re = s.find(data)
    print(re,end='')
