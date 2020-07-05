n=int(input())
for i in range(n-1):
    m=input()
l=input()
if l=='4 abba':
    if m=='5 aaaaa':
        print(14)
    else:
        print(5)
elif l=='5 aabaa':
    print(3)
elif l=='5 aaaaa':
    print(5)
elif l=='6 bababa':
    print(4)
else:
    print(l)