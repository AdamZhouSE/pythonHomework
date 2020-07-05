happy_nums = [1, 7, 10, 13, 19, 23, 28, 31, 32, 44, 49, 68, 70, 79, 82, 86, 91, 94, 97, 100]
unhappy_nums = [4, 16, 37, 58, 89, 145, 42, 20]


def is_happy_num(num):
    if num == 0:
        return False
    if num < 10:
        if num * num in happy_nums:
            return True
        elif num * num in unhappy_nums:
            return False
        else:
            return is_happy_num(num*num)
    if num < 100:
        a = int(num/10)
        b = num % 10
        if a * a + b * b in happy_nums:
            return True
        elif a*a + b*b in unhappy_nums:
            return False
        else:
            return is_happy_num(a*a + b*b)
    if num < 1000:
        a = int(num/100)
        b = int((num%100)/10)
        c = num%10
        if a*a + b*b + c*c in happy_nums:
            return True
        elif a*a + b*b + c*c in unhappy_nums:
            return False
        else:
            return is_happy_num(a*a + b*b + c*c)
    if num < 10000:
        a = int(num/1000)
        b = (num%1000)/100
        c = (num%100)/10
        d = num%10
        if a*a + b*b + c*c + d*d in happy_nums:
            return True
        elif a*a + b*b + c*c + d*d in unhappy_nums:
            return False
        else:
            return is_happy_num(a*a + b*b + c*c + d*d)


if __name__ == '__main__':
    n = int(input())
    print(is_happy_num(n))

