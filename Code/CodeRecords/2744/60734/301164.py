def isPalindrome(string):
    left,right = 0,len(string)-1
    while left<=right:
        if string[left]!=string[right]:
            return False
        left+=1
        right-=1
    return True

n = int(input())
strings = []
for i in range(n):
    l, string = input().split(' ')
    strings.append(string)

cnt = 0
for a in strings:
    for b in strings:
        if isPalindrome(a+b):
            cnt+=1
print(cnt)