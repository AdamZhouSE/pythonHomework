def rev(a):
    count = 0
    for i in range(len(a)):
        count += int(a[i]) * pow(10, i)
    return count
a = input()
if a[0] =='-':
    print(rev(a[1:len(a)])-2*rev(a[1:len(a)]))
else:
    print(rev(a))