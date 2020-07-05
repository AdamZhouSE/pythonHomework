def huffman_tree(weights: list):
    queue = []
    for i in range(len(weights)):
        queue.append(int(weights[i]))
    ans = 0
    while len(queue) > 1:
        queue.sort()
        a = queue.pop(0)
        b = queue.pop(0)
        ans += a + b
        queue.append(a + b)
    return ans


if __name__ == '__main__':
    n = input()
    power_of_leaves = input().split()
    print(huffman_tree(power_of_leaves))