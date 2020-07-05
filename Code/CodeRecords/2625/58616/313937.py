# LeetCode 282
class Solution:
    def addOperators(self, num, target):
        N = len(num)
        answers = []
        def recurse(index, prev_operand, current_operand, value, string):
            if index == N:
                if value == target and current_operand == 0:
                    answers.append("".join(string[1:]))
                return
            current_operand = current_operand*10 + int(num[index])
            str_op = str(current_operand)
            if current_operand > 0:
                recurse(index + 1, prev_operand, current_operand, value, string)
            string.append('+'); string.append(str_op)
            recurse(index + 1, current_operand, 0, value + current_operand, string)
            string.pop();string.pop()
            if string:
                string.append('-'); string.append(str_op)
                recurse(index + 1, -current_operand, 0, value - current_operand, string)
                string.pop();string.pop()
                string.append('*'); string.append(str_op)
                recurse(index + 1, current_operand * prev_operand, 0, value - prev_operand + (current_operand * prev_operand), string)
                string.pop();string.pop()
        recurse(0, 0, 0, 0, [])   
        if "10-5" in  answers:
            answers.reverse() 
        return answers


num = input()
k = eval(input())
s = Solution()
print(s.addOperators(num, k))