#感觉写法有问题
s=input()
k=int(input())
if k>1:
    a=list(s)
    a.sort()
    print(''.join(str(i) for i in a))
else:
    min_value=ord('z')
    min_index=0
    for i in range(len(s)):
        if ord(s[i])<min_value:
            min_value=ord(s[i])
            min_index=i
    print(s[min_index:]+s[0:min_index])            