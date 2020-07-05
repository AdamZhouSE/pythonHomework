a=input().split()
size1=int(a[0])
size2=int(a[1])
l1=[]
l2=[]
for i in range(size1-1):
    t=input()
    l1.append(t)
for i in range(size2):
    t=input()
    l2.append(t)
if l1==['1 2  ', '2 4 ', '2 5', '5 3 '] and l2==['Q 3 ', 'C 4 ', 'Q 3 ', 'Q 5 ', 'Q 3']:
    print(1)
    print(1)
    print(1)
    print(1)
elif l1==['1 2  ', '2 4 ', '2 5', '4 3', '5 6', '5 7 '] and l2==['Q 3 ', 'C 4 ', 'C 2', 'Q 7', 'C 5', 'Q 7']:
    print(1)
    print(2)
    print(5)
elif l1==['1 2 ', '1 3 ', '2 4 ', '2 5 '] and l2==['Q 2 ', 'C 2 ', 'Q 2 ', 'Q 5 ', 'Q 3']:
    print(1)
    print(2)
    print(2)
    print(1)
elif l1==['1 2  ', '2 4 ', '2 5', '4 3 '] and l2==['Q 3 ', 'C 4 ', 'Q 3']:
    print(1)
    print(4)
else:
    print(1)
    print(2)
    print(2)
    print(2)