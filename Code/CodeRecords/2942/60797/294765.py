class Solution:

    def permutations(self, arr, position, end):
        global re
        if position == end:
            re.append(eval((str(arr))))

        else:
            for index in range(position, end):
                arr[index], arr[position] = arr[position], arr[index]
                self.permutations(arr, position + 1, end)

    def find(self, n, data):
        global re
        re = []
        self.permutations(data, 0, len(data))
        return max(re)

if __name__ == '__main__':
    n = int(input())
    data = input().split()
    s = Solution()
    res = s.find(n, data)
    print(res)
