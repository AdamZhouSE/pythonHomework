l=input().split(" ")
n=int(l[0])
x=int(l[1])
list=input().split(" ")
for i in range(n- 1):  
        for j in range(n - i - 1):  
            if int(list[j]) > int(list[j + 1]):
                list[j], list[j + 1] = list[j + 1], list[j]
result=0
for i in list:
    if x>1:
        result+=int(i)*x
        x-=1
    else:
        result+=int(i)
print(result)