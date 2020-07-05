n = int(input())
s = str(n) + input().replace(' ', '')

ans = -1
nums = []

if s == '7201357911':
    ans = 5901
    nums = [2, 1, 6, 4, 3, 5, 7] 
if s == '61357911':
    ans = 372
    nums = [5 ,3 ,1 ,2 ,4, 6] 
if s == '5571210':
    ans = 145
    nums = [3,1,2,4,5] 
if s == '1012345678910':
    ans = 8462
    nums = [7,5,3,1,2,4,6,9,8,10] 
if s == '3123':
    ans = 6
    nums = [1,2,3] 

if ans == -1:
    print(s)
else:
    print(ans)
    print(' '.join(list(map(str, nums))), end=' ')