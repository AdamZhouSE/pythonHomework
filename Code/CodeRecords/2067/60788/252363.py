class Solution(object):
    def intToRoman(self, num):
        if num > 3999 or num < 1:
            return 0        
        num_tuple = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        roman_tuple = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']      
        result_str = ""
        
        for i in range(len(num_tuple)):
            
            while num >= num_tuple[i]:
                num -= num_tuple[i]
                result_str += roman_tuple[i]
        return result_str


s = Solution()
print(s.intToRoman(int(input())))
