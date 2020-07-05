s1=input()
s2=input()
from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # 第一个字符串的长度
        len_s1 = len(s1)
        # 第二个字符串的长度
        len_s2 = len(s2)
        # 如果第一个字符串短于第二个，肯定是 False
        if len_s1 > len_s2:
            return False
        else:
            # 第一个字符串中各个字符的个数
            c_s1 = Counter(s1)
            # 从左边开始，长度和第一个字符串相等的子字符串中各个字符的个数
            c_s2 = Counter(s2[0:len_s1])
            # 在第二个子字符串中，从左往右移动
            l_index = 0
            while c_s1 != c_s2:
                # 如果不能继续往右移动了,则返回没有找到
                if l_index+len_s1 == len_s2:
                    return False
                # 向右移动一步，把最左边的剔除，最右边的加入
                # 需要删除的
                to_be_removed = s2[l_index]
                # 需要增加的
                to_be_added = s2[l_index+len_s1]
                l_index += 1
                if to_be_removed == to_be_added:
                    continue
                c_s2[to_be_removed] -= 1
                if c_s2[to_be_removed] == 0:
                    del c_s2[to_be_removed]
                c_s2[to_be_added] += 1
            return True
