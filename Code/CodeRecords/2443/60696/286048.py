class Node:
    def __init__(self, num, n):
        self.num = num
        self.value = num
        self.value += num[0] * (n-len(self.value))


if __name__ == '__main__':
    nums = [str(i) for i in input()[1:-1].split(',')]
    n = max([len(i) for i in nums])
    values = [Node(num, n) for num in nums]
    values.sort(key=lambda x: x.value, reverse=True)
    res = ''
    for value in values:
        res += value.num
    print(int(res))