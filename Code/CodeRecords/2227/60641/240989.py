def main():
    n = int(input())
    k = int(input())
    passwords = set()
    result = []
    find("0" * (n - 1), n, k, passwords, result)
    print(("".join(result) + "0" * (n - 1))[::-1])


def find(s, n, k, passwords, result):
    for i in range(0, k):
        temp = s + str(i)
        if temp not in passwords:
            passwords.add(temp)
            find(temp[1:], n, k, passwords, result)
            result.append(str(i))


if __name__ == '__main__':
    main()


"""
欧拉回路的问题
设n=3，k=3，那么则有9个节点，其中有27个边，代表了27个密码类型
一开始将00设为起点，然后若取得1，则是00-->01
中间这条边代表了001这样的一个密码
因此，代码中任意的走完没走过的边
最终会形成一个欧拉回路
"""