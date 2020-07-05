def func(s:str):
    res=0
    length=len(s)
    for i in range(1,length+1):
        for j in range(length-i+1):
            temp=s[j:j+i]
            if temp.count('0')==temp.count('1') and temp.count('0')==temp.count('2'):
                res+=1
    return res

tests=int(input()) #找规律
lists=[]
for i in range(tests):
    lists.append(input())
for i in lists:
    print(func(i))