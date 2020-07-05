RomanLetter = ['I','V','X','L','C','D','M']


#i代表从右往左第几位
def letter(n,i):
    if n == 9:
        return RomanLetter[2*i] + RomanLetter[2*i+2]
    if n == 4:
        return RomanLetter[2*i] + RomanLetter[2*i+1]
    val = ""
    for j in range(n%5):
        val += RomanLetter[2*i]
    if n == 5:
        val = RomanLetter[2*i+1] + val
    return val

def Int2Roman(n):
    i = 0
    res = ""
    while n > 0:
        res = letter(n%10,i) + res
        i = i + 1
        n = int(n / 10)
    return res

if __name__ == "__main__":
    n = int(input())
    print(Int2Roman(n))