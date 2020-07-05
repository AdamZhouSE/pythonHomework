def del_elements(arr):
    odd_num,even_num=[],[]
    for x in arr:
        if x%2:odd_num.append(x)
        else:even_num.append(x)
    res=0
    if abs(len(odd_num)-len(even_num))<=1:return 0
    if len(odd_num)>len(even_num):
        odd_num.sort()
        for i in range(len(odd_num)-len(even_num)-1):
            res+=odd_num[i]
    elif len(even_num)>len(odd_num):
        even_num.sort()
        for i in range(len(even_num)-len(odd_num)-1):
            res+=even_num[i]
    return res


n = int(input())
arr=list(map(int,input().split()))
print(del_elements(arr))