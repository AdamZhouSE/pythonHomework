class Solution:
    def baseNeg2(self, N: int) -> str:
        def num_to_n_scale(n, x):
            """

            :param n: 待转换10进制数
            :param x: 转换为x进制，x < 0
            :return: 返回x进制的字符串
            """
            import math
            buff = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", 'A', 'B', 'C', 'D', 'E', 'F']
            b = []
            x = int(x)

            while True:
                abs_x = abs(x)
                s = math.ceil(n / x)  # 商
                y = (abs_x - abs(n % x)) % abs_x  # 余数
                b.append(buff[y])
                if s == 0:
                    break
                n = s
            return "".join(reversed(b))

        return num_to_n_scale(N, -2)


if __name__=="__main__":
    n=int(input())
    print(Solution().baseNeg2(n))