def numberToWords(num: int) :
    w3 = [" Thousand", " Million", " Billion"]
    w2 = [" Twenty", " Thirty", " Forty", " Fifty", " Sixty", " Seventy", " Eighty", " Ninety"]
    w1 = [" One", " Two", " Three", " Four", " Five", " Six", " Seven", " Eight", " Nine", " Ten", " Eleven", " Twelve",
          " Thirteen", " Fourteen", " Fifteen", " Sixteen", " Seventeen", " Eighteen", " Nineteen"]
    if num == 0:
        return "Zero"
    n = ''
    i = 0
    while num:
        j = ''
        k = num % 1000
        num = num // 1000
        if num % 1000:
            j = w3[i]

        if k // 100:
            j += w1[k // 100 - 1] + " Hundred"
            k = k % 100
        if k > 19:
            j += w2[k // 10 - 2]
            k = k % 10
        if k:
            j += w1[k - 1]

        i += 1
        n = j + n
    return n.strip()

if __name__ == '__main__':
    n = int(input())
    print(numberToWords(n))