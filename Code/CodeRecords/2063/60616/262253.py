def isPalindrome(x):
    s = str(abs(x))
    s1 = s[::-1] 
    s2 = int(s1) 
    if x == s2: 
        print(True)
    else:
        print(False)

s=int(input())
isPalindrome(s)