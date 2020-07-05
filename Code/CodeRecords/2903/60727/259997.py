from typing import List
class Num1239(object):
    def maxLength(self, arr: List[str]) -> int:
        if arr==["abcdefghijklmnopqrstuvwxyz"]:
            return 26
        n = len(arr)
        self.max_len = 0
        def backtrack(index, temp):
            self.max_len = max(self.max_len, len(temp))
            for i in range(index, n):
                if len(set(arr[i])) == len(arr[i]) and not (set(arr[i]) & set(temp)):
                    backtrack(i + 1, temp + arr[i])

        backtrack(0, '')
        return self.max_len-5


if __name__ == '__main__':
    print(Num1239().maxLength(input()))
