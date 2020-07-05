def str_sort(s):
    if len(s) <= 1:
        return [s]
    str_list = []
    for i in range(len(s)):
        for j in str_sort(s[0:i] + s[i + 1:]):
            str_list.append(s[i] + j)
    return str_list
n=input()
str1=""
for i in range(int(n)):
    a=str(i+1)
    str1+=a
k=int(input())
print(str_sort(str1)[k-1])
    