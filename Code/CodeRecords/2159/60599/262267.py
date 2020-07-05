class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num > 3999 or num < 1:
            return 0
        # 字典是无序的，所以不使用字典
        # 注意这里一定要是倒序，否则执行会有问题，让数从大往小查找适合的罗马数
        num_tuple = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        roman_tuple = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
        # 记录结果的字符串
        result_str = ""
        # 从整数的列表中开始遍历
        for i in range(len(num_tuple)):
            # 从大往小开始判断，num小于当前数则进行下一次循环
            # num大于当前数则进行减法运算，并取出相应位置的Roman数
            while num >= num_tuple[i]:
                num -= num_tuple[i]
                result_str += roman_tuple[i]
        return result_str


if __name__ == '__main__':
    s = Solution()
    print(s.intToRoman(int(input())))

