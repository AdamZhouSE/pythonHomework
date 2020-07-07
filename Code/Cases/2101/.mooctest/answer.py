class Solution:
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        mem = set()                #利用 set（）集合，保存平方求和后的数值
        while n != 1:              #利用 while 实现循环
            n = sum([int(i)**2 for i in str(n)])    #通过str（n）调取输入整数各个位数的值
            if n not in mem:       #若平方求和后的数值是首次出现，则添加进集合中
                mem.add(n)
            else:                  #若求和后数值，在集合中存在，则直接返回false,即出现死循环
                return False
        return True                #最终当n==1时，跳出while循环，返回true
a = input()
s = Solution()
print(s.isHappy(int(a)))