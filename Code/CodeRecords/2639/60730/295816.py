class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if s == "":
            return 0
        left = 0
        right = 0
        char_max = 0
        word_num = {}
        for right in range(len(s)):
            word_num.setdefault(s[right], 0)
            word_num[s[right]] += 1
            char_max = max(char_max, word_num[s[right]])
            if right - left + 1 > char_max + k:
                word_num[s[left]] -= 1
                left += 1
        return len(s) - left


if __name__ == "__main__":
    m = input()
    n = int(input())
    solution = Solution()
    result = solution.characterReplacement(m, n)
    print(result)
