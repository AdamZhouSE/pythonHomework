class Solution:
    def isPalindrome(self, data):
        for i in range(len(data)):
            if data[i]!=data[len(data)-1-i]:
                return False
        return True
            
            
    def find(self, data):
        re = 0
        for i in range(len(data)):
            for j in range(i,len(data)):
                if self.isPalindrome(data[i,j+1]):
                    re +=1
        return re


if __name__ == '__main__':
    ss = input()
    data = ss
    q = int(input())
    for i in range(q):
        line = input().split()
        if line[0]==1:
            data = data+line[1]
        elif line[0]==2:
            data = line[1][::-1]+data
        elif line[0]==3:
            s = Solution()
            re = s.find(data)
            print(re)
