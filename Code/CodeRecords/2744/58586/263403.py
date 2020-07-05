nums=int(input())
words=[]
for i in range(nums):
    words.append(input().split(" ")[1])
def isPalindrome(s):
    left=0
    right=len(s)-1
    while left<right:
        if s[left]!=s[right]:
            return False
        left+=1
        right-=1
    return True
count=0
for i in range(nums):
    for j in range(nums):
        newStr=words[i]+words[j]
        if isPalindrome(newStr):
            count+=1
print(count)