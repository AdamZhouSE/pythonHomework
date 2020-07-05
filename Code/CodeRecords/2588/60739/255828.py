def factorization(num):
    factor = []
    while num > 1:
        for i in range(num - 1):
            k = i + 2
            if num % k == 0:
                factor.append(k)
                num = int(num / k)
                break
    return factor

def sum(str):
    sum = 0
    for i in range (len(str)):
        tmp = int(str[i])
        sum += tmp
    return sum

def isSmith(num, list):
    num_sum = sum(str(num))
    list_sum = 0
    for i in range (len(list)):
        tmp = sum(str(list[i]))
        list_sum += tmp
    if num_sum == list_sum:
        return True
    else:
        return False

if __name__ == '__main__':
    c = int(input())
    n_list = []
    ans = []
    for i in range (c):
        n = int(input())
        p = int(isSmith(n, factorization(n)))
        n_list.append(n)
        if len(factorization(n)) == 1:
            p = 0
        ans.append(p)
        print(p)

