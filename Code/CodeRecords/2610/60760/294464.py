def func(s:str):   #遍历一遍所有的子串
    res=0
    length=len(s)
    for i in range(1,length+1):
        for j in range(length-i+1):
            temp=s[j:j+i]
            l=len(temp)
            if len(set(temp))==l:
                res+=l
    return res

tests=int(input()) #找规律
lists=[]
for i in range(tests):
    a=input()
    lists.append(''.join(input().split(' ')))
for i in lists:
    print(func(i))