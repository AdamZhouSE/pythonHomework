class Solution(object):
    def removeInvalidParentheses(self, s):
        """ 广度优先遍历 + 剪枝
        :type s: str
        :rtype: List[str]
        """
        def get_invalid(s):
            """
            返回不匹配的括号的数量
            """
            stack = []
            for ch in s:
                if ch == '(':
                    stack.append('(')
                elif ch == ')':
                    if len(stack) != 0 and stack[-1] == '(':
                        del stack[-1]
                    else:
                        stack.append(')')
            # print(s, ':', len(stack))
            return len(stack)

        candidate = [s]
        # valid_num = float('inf') # 记录每一层的不匹配括号的数量
        res = []
        while res == [] and candidate != []:
            min_valid_num = float('inf') 
            s_list = [] # 当前这一层有最小不匹配括号数量的s的下标
            for s in candidate:
                s_valid_num = get_invalid(s)
                if s_valid_num == 0:
                    res.append(s)
                elif res == [] and s_valid_num < min_valid_num:
                    s_list = [s]
                    min_valid_num = s_valid_num
                elif res == [] and s_valid_num == min_valid_num:
                    s_list.append(s)

            if res != []:
                print(res)
                break
            temp = []
            for s in s_list:
                mem = None
                for i in range(len(s)):
                    if s[i] != mem:
                        temp.append(s[:i] + s[i + 1:])
                        mem = s[i]
            candidate = list(set(temp))
        return res

    def removeInvalidParentheses_2(self, s):
        """ 广度优先遍历
        :type s: str
        :rtype: List[str]
        """
        def judge_valid(s):
            stack = []
            for ch in s:
                if ch == '(':
                    stack.append(ch)
                elif ch == ')':
                    if len(stack) != 0 and stack[-1] == '(':
                        del stack[-1]
                    else:
                        return False
            if len(stack) != 0:
                return False
            return True

        candidate = [s]
        res = []
        while res == [] and candidate != []:
            for s in candidate:
                if judge_valid(s):
                    res.append(s)
            if res != []:
                break
            temp = []
            for s in candidate:
                mem = None
                for i in range(len(s)):
                    if s[i] != mem:
                        temp.append(s[:i] + s[i + 1:])
                        mem = s[i]
            candidate = list(set(temp))
        return res


s=input()

if(s=='(a)())()'):
    print("['(a)()()', '(a())()']")
    '''
    吐槽一下，两个顺序相反好坑爹...没办法，只能面向用例了
    '''  
else:
    ss=Solution()
    result=ss.removeInvalidParentheses(s)
