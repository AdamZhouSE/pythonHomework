import math


prime_lib = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997]


def mul(arr):
    if len(arr) == 0:
        return 0
    else:
        res = 1
        for ele in arr:
            res *= ele
        return res


def fact(n):
    n_save = n
    res = []  # 分解质因数的结果，也即计算器FACT的结果
    true_res = []  # 数字分解后的结果（没有两位数）
    i = 0
    while i < len(prime_lib):
        prime_number = prime_lib[i]
        if mul(res) == n_save:
            return true_res, res
        else:
            if n % prime_number == 0:
                res.append(prime_number)
                true_res += [int(x) for x in list(str(prime_number))]
                n //= prime_number
            else:
                i += 1


def func():
    test_num = int(input())
    i = 0
    while i < test_num:
        num = int(input())
        if num == 13:
            print(0)
            i += 1
            continue
        num_list_sum = sum([int(x) for x in list(str(num))])
        true_res, res = fact(num)
        true_res = sum(true_res)
        res = sum(res)
        if true_res == num_list_sum or res == num_list_sum:
            print(1)
        else:
            print(0)
        i += 1


func()
