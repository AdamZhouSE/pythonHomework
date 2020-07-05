a = input()
a = list(map(int, a[1:len(a) - 1].split(",")))
t = int(input())
start = 0
end = len(a)-1
while start != end:
    mid = (start+end)//2
    if start == end -1:
        if t == a[start]:
            end = start
        elif t == a[end]:
            start = end
        else:
            start = -1
            end = -1
        break
    else:
        if t > a[mid]:
            start = mid
        elif t < a[mid]:
            end = mid
        else:
            break
print((start+end)//2)