import math
"""
如果一个正整数自身是回文数，而且它也是一个回文数的平方，那么我们称这个数为超级回文数
现在，给定两个正整数 L 和 R （以字符串形式表示），返回包含在范围 [L, R] 中的超级回文数的数目
"""

def isplalindrome(n):
    if(math.ceil(n)!=math.floor(n)):
        return False
    else:
        n=int(n)
    arr=[int(m) for m in list(str(n))]
    i=0
    while(i<len(arr)//2):
        if(arr[i]!=arr[len(arr)-1-i]):
            return False
        i+=1
    return True


L=int(input())
R=int(input())

result=0
while(L<=R):
    if(isplalindrome(L) and isplalindrome(math.pow(L,0.5))):
        result+=1
    L+=1

print(result)