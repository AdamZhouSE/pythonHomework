def ed(S):
    def search(L, a, modulus, n, nums):
        h = 0
        for i in range(L):
            h = (h * a + nums[i]) % modulus
        seen = {h}
        aL = pow(a, L, modulus)
        for start in range(1, n - L + 1):
            h = (h * a - nums[start - 1] * aL + nums[start + L - 1]) % modulus
            if h in seen:
                return start
            seen.add(h)
        return -1

    n = len(S)
    nums = [ord(S[i]) - ord('a') for i in range(n)]
    a = 26
    modulus = 2 ** 32
    left, right = 1, n
    while left != right:
        L = left + (right - left) // 2
        if search(L, a, modulus, n, nums) != -1:
            left = L + 1
        else:
            right = L
    start = search(left - 1, a, modulus, n, nums)
    print(S[start: start + left - 1] if start != -1 else "")
if __name__ == '__main__':
    ed(input())
