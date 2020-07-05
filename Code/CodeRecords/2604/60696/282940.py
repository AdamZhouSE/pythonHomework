class Solution:
    def min_letter(self, letters:list, target:str)->str:
        n = len(letters)
        i = 0
        while True:
            if letters[i] > target:
                break
            i += 1
            if i >= n:
                i = i % n
                break
        return letters[i]


if __name__ == '__main__':
    letters = eval(input())
    target = input()
    print(Solution().min_letter(letters, target))