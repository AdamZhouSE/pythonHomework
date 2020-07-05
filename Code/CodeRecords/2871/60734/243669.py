n = int(input())
lst = input().split(' ')
lst = list(map(int,lst))

if lst.count(2)<= lst.count(1):
    res = lst.count(2)+(lst.count(1)-lst.count(2))//3
else:
    res = lst.count(1)
print(res)