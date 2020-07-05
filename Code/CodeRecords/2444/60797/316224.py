class Solution:
    def find(self):
        for i in range(len(nums) - k):
            for j in range(i, i + k):
                if abs(nums[i] - nums[j]) == t:
                    return True
        return False

if __name__ == '__main__':
    s = input().split()  # s=['nums' , '=' , '[?,?,?],' , 'k' , '=' , '?,' , 't' , '=' , '?']
    nums = [int(a) for a in s[2].strip('[],').split(',')]
    k = int(s[5][:-1])
    t = int(s[8])
    ss = Solution()
    if ss.find():
        print('true')
    else:
        print('false')
                
