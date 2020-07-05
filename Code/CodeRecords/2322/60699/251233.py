L=input()
R=input()
L, R = int(L), int(R)
MAGIC = 100000

def is_palindrome(x):
    list1=list(str(x))
    list1.reverse()
    return x == int("".join(list1))

ans = 0


for k in range(0,MAGIC):
    s = str(k) 
    t = s + s[-2::-1] 
    v = int(t) ** 2
    if v > R: break
    if v >= L and is_palindrome(v):
        ans += 1


for k in range(0,MAGIC):
    s = str(k) 
    t = s + s[::-1] 
    v = int(t) ** 2
    if v > R: break
    if v >= L and is_palindrome(v):
        ans += 1

print(ans)