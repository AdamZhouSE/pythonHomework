def bin_add(s1, s2):
    lena = len(s1)
    lenb = len(s2)
    if lena < lenb:
        a = s1
        s1 = s2
        s2 = a
    ss2 = '0' * abs(lena - lenb) + s2
    ans = ''
    carry = 0
    for i in range(max(lena, lenb)):
        sum = int(s1[-i-1]) + int(ss2[-i-1]) + carry
        if sum >= 2:
            carry = sum//2
            ans = str(sum%2) + ans
        else:
            carry = 0
            ans = str(sum) + ans
    if carry == 1:
        ans = '1' + ans
    return ans


if __name__ == "__main__":
    s1 = input()
    s2 = input()
    print(bin_add(s1, s2))
