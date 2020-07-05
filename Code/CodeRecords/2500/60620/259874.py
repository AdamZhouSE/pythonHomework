a=eval(input())
result=[]
def f(a):
    max_num = max(a)
    min_num = min(a)
    if len(a) == 1:
        return result
    elif max_num == a[-1]:
        return f(a[:-1])
    elif(min_num == a[-1] or max_num == a[0]):
        result.append(len(a))
        a= list(reversed(a))
        return f(a)
    else:
        for i in range(len(a)):
            if a[i] == max_num:
                break
        a[:i+1] = a[i::-1]
        result.append(i+1)
        return f(a)
print(f(a))