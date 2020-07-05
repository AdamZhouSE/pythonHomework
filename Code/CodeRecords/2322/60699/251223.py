L=input()
R=input()
L, R = int(L), int(R)
MAGIC = 100000

def reverse(x):
    ans = 0
    while x:
        ans = 10 * ans + x % 10
        x /= 10
    return ans

def is_palindrome(x):
    return x == reverse(x)

ans = 0


for k in range(0,MAGIC):
    s = str(k)  # Eg. s = '1234'
    t = s + s[-2::-1]  # t = '1234321'
    v = int(t) ** 2
    if v > R: break
    if v >= L and is_palindrome(v):
                ans += 1L=input()
R=input()
L, R = int(L), int(R)
MAGIC = 100000


def is_palindrome(x):
    list1=list(str(x))
    list1.reverse()

    return x == int("".join(list1))

ans = 0


for k in range(0,MAGIC):
    print(k)
    s = str(k)  # Eg. s = '1234'
    t = s + s[-2::-1]  # t = '1234321'
    v = int(t) ** 2
    print(v)
    if v > R: break
    if v >= L and is_palindrome(v):
        ans += 1


for k in range(0,MAGIC):
    s = str(k)  # Eg. s = '1234'
    t = s + s[::-1]  # t = '12344321'
    v = int(t) ** 2
    if v > R: break
    if v >= L and is_palindrome(v):
        ans += 1

print(ans)


for k in range(0,MAGIC):
    s = str(k)  # Eg. s = '1234'
    t = s + s[::-1]  # t = '12344321'
    v = int(t) ** 2
    if v > R: break
    if v >= L and is_palindrome(v):
        ans += 1


print(ans)