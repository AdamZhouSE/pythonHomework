"""
给定字符串“ s”。任务是查找最小窗口长度，该窗口长度至少包含一次给定字符串的所有字符
例如。 A =“ aabcbcdbca”，那么结果将是4，因为最小的窗口将是“ dbca”
"""

def get_str(s):
    set1=set(s)
    return "".join(set1)


n=int(input())
str_list=[]

for i in range(n):
    str_list.append(str(input()))

for i in range(n):
    arr=list(str_list[i])
    str=list(get_str(arr))

    min_len=len(arr)
    for begin in range(len(arr)):
        end=begin+len(str)+1
        while end<=len(arr):
            bool = True
            for ch in str:
                if ch not in arr[begin:end]:
                    bool = False
                    break
            if bool and (end-begin-1)<min_len:
                min_len=end-begin-1
            end+=1

    print(min_len)