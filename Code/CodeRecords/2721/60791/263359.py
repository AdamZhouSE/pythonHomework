def solve(s1,s2):
    res =  val(s1)*val(s2)
    print(res)
    return
def val(s):
    res = 0
    for i in range(len(s)):
        if(s[i] == '1'):
            res += 2**(len(s)-i-1)
    return res

T = int(input())
x = 0
while(x<T):
    x+=1
    arr = input().split(' ')
    solve(arr[0],arr[1])
    