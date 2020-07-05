import math


def deci_eng(nums):
    for i in range(1, 5):
        if len(nums) < 3*i:
            k = 3*i-len(nums)
            while k>0:
                nums.insert(0, '0')
                k -= 1
            break

    ans = ''
    for j in range(0, i):
        ans = ans + get_three(int(nums[j*3]), int(nums[j*3+1]), int(nums[j*3+2]), i-1-j) + ' '
    return ans.strip()


def get_three(a, b, c, bits):
    dic = {1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five', 6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine', 10: 'Ten',
           11: 'Eleven', 12: 'Twelve', 13: 'Thirteen', 14: 'Fourteen', 15: 'Fifteen', 16: 'Sixteen', 17: 'Seventeen',
           18: 'Eighteen', 19: 'Nineteen', 20: 'Twenty', 30: 'Thirty', 40: 'Forty', 50: 'Fifty', 60: 'Sixty',
           70: 'Seventy',
           80: 'Eighty', 90: 'Ninety', 100: 'Hundred', 1000: 'Thousand', 1000000: 'Million', 1000000000: 'Billion'}

    ans = ''
    if a != 0:
        ans = dic[a] + ' ' + dic[100]
        if b != 0 or c != 0:
            ans += ' '
            temp = int(str(b) + str(c))
            if b != 0 and dic.__contains__(temp):
                ans += dic[temp]
            elif b != 0:
                tens = int(str(b) + '0')
                ans += dic[tens]
                if c != 0:
                    ans = ans + ' ' + dic[c]
            elif b == 0:
                if c != 0:
                    ans = ans + 'and ' + dic[c]
    else:
        if b != 0 or c != 0:
            ans += ' '
            temp = int(str(b) + str(c))
            if dic.__contains__(temp):
                ans += dic[temp]
            elif b != 0:
                tens = int(str(b) + '0')
                ans += dic[tens]
                if c != 0:
                    ans = ans + ' ' + dic[c]
            elif b == 0:
                if c != 0:
                    ans = ans + 'and ' + dic[c]
    if (a != 0 or b != 0 or c != 0) and bits > 0:
        expo = math.pow(10, bits * 3)
        ans = ans + ' ' + dic[expo]
    return ans


if __name__ == "__main__":
    n = list(input())
    print(deci_eng(n))
