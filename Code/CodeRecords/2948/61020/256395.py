'''第一步： 取出姓名的缩写（abbreviation）并接在一起。例如，如果这对恋人叫 Jiang Yun Fan 和 Tang Yu Rou，他们的缩写就是 JYFTYR。
第二步： 将每个字母用数字字符串取代。用 ST 来取代 A， ST+1 来取代 B， ST+2 来取代 C，……， ST+25 来取代 Z，其中 ST 为一个已知的
正整数。例如，如果ST=81，A 就被 81 取代，B 就被 82 取代，……，Z 则被 106 取代。上面的例子JYFTYR 则被 901058610010598 取代。
第三步：重复以下操作：将相邻的两位数相加，并写下和的个位数。不难发现这个操作每进行一次，这个数字字符串就会少一位数。当这个数字变
成 100 或不超过两位数（第一位是 0 也算两位数）时，这个程序便停止。所得的数字就是两人的缘分。用上面的例子来说，处理的过程如下：

901058610010598

91153471011547

0268718112691

…… 374 01

所以如果 ST=81，Jiang Yun Fan 和 Tang Yu Rou 的缘分便只有 1。'''


def abbr_to_num_list(abbr, ST):
    # tested

    result = []

    for char1 in abbr:
        current_num = ST + ord(char1) - ord('A')
        for char2 in str(current_num):
            result.append(int(char2))

    return result


def num_list_to_str(num_list):
    result = ''
    for num in num_list:
        result += str(num)

    return result


def num_list_to_combined_num(num_list):
    return int(num_list_to_str(num_list))


def one_time_reduced_num_list(num_list):
    if len(num_list) == 2:
        return [(num_list[0] + num_list[1]) % 10]

    result = one_time_reduced_num_list(num_list[:-1])
    result.append((num_list[-2] + num_list[-1]) % 10)
    return result


def num_list_to_yuan_fen(num_list):
    if num_list_to_combined_num(num_list) <= 100:
        return num_list_to_combined_num(num_list)

    return num_list_to_yuan_fen(one_time_reduced_num_list(num_list))


if __name__ == "__main__":
    # s = input()
    print(num_list_to_yuan_fen(abbr_to_num_list(input(), int(input()))), end='')

# print(ord('a'))
# print(ord('b'))
# print(ord('c'))
# print(ord('d'))
# print(ord('e'))
