def sumup(k,n,max_n,numbers):
    if k == 1:
        if n>max_n:
            numbers.append(n)
            res.append(numbers.copy())
            numbers.pop()
        return
    
    if n <= 9: maxnumber = n
    else: maxnumber = 9
    for i in range(max_n,maxnumber):
        if i not in numbers:
            numbers.append(i)
            sumup(k-1,n-i,i,numbers)
            numbers.pop()

lst = list(input().split(','))
k = int(lst[0])
n = int(lst[0])

res = []
sumup(3,11,1,[])
print(res)