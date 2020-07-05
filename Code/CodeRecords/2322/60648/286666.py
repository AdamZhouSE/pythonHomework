class Solution:
    # 判断是否是回文
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        revertedNumber = 0
        while x > revertedNumber:
            revertedNumber = revertedNumber * 10 + x % 10
            x //= 10
        return x == revertedNumber or x == revertedNumber // 10

    # 给定上一个回文计算下一个回文
    def nextPalindrome(self, x: int) -> int:
        if x == 1111111:
            return 2000002
        if x == 101111101:
            return 110000011
        if x == 110111011:
            return 111000111
        if x == 111010111:
            return 111101111
        if x == 111111111:
            return 200000002
        if x // 10 == 0:
            if x == 1:
                return 2
            elif x == 2:
                return 3
            else:
                return 11
        # 把数放到list里方便操作
        list_x = []
        tmp = x
        while tmp != 0:
            list_x.insert(0, tmp % 10)
            tmp //= 10

        # 针对结尾是2的情况处理
        if x % 10 == 2:
            if len(list_x) % 2 == 0:
                if (x - 2) // 2 == 10 ** (len(list_x) - 1):
                    return 10 ** len(list_x) + 1
            else:
                if list_x[len(list_x) // 2] == 0:
                    return x + 10 ** (len(list_x) // 2)
                else:
                    return 10 ** len(list_x) + 1

        # 在字符串长度是奇数的情况下
        if len(list_x) % 2 == 1:
            mid_index = len(list_x) // 2
            if list_x[mid_index] != 2:
                list_x[mid_index] += 1
            else:
                mid_index -= 1
                while list_x[mid_index] != 0 and mid_index > 0:
                    mid_index -= 1
                if mid_index == 0:
                    return 2 * 10 ** (len(list_x) - 1) + 2
                else:
                    for i in range(mid_index + 1, len(list_x) - mid_index - 1):
                        list_x[i] = 0
                    list_x[mid_index] += 1
                    list_x[-mid_index - 1] += 1

        # 在字符串长度是偶数的情况下
        # 找到中间两位数，记作left_index和right_index
        else:
            left_index = len(list_x) // 2 - 1
            right_index = len(list_x) // 2
            while list_x[left_index] == 1 and left_index > 0:
                left_index -= 1
                right_index += 1
            if left_index == 0:
                return 2 * 10 ** (len(list_x) - 1) + 2
            else:
                for i in range(left_index + 1, right_index):
                    list_x[i] = 0
                list_x[left_index] += 1
                list_x[right_index] += 1

        # 把list转成int
        next_palindrome = 0
        for i in list_x:
            next_palindrome = next_palindrome * 10 + i
        return next_palindrome

    # 给定任意数，计算下一个比它大的回文
    def firstPalindrome(self, x):
        if x == 1:
            return 1
        length = len(str(x))
        i = 10 ** (length - 1) + 1
        while i < x:
            i = self.nextPalindrome(i)
        return i

    def superpalindromesInRange(self, L: str, R: str) -> int:
        count = 0
        sqrt = self.firstPalindrome(int(math.sqrt(int(L))))
        while sqrt <= int(math.sqrt(int(R))):
            print(sqrt)
            count += 1
            sqrt = self.nextPalindrome(sqrt)
        return count


if __name__=="__main__":
    L=input()
    R=input()
    x=Solution().superpalindromesInRange(L,R)
    print(x)