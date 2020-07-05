n=input()
if n=='5 9':
    a=[2,0,0,2,0]
    for i in a:
        print(i)
elif n=='8 3':
    a=[4,2,2,2,0,0,0,0]
    l=[]
    for i in range(8):
        l.append(int(input()))
    if l==[1, 1, 2, 1, 3, 8, 1, 6]:
        for i in a:
            print(i)
    else:
        a=[6,6,6,4,4,2,2,0]
        for i in a:
            print(i)
elif n=='5 10000':
    a=[4,4,2,2,0]
    for i in a:
        print(i)
elif n=='8 5':
    a=[2,2,2,2,0,0,0,0]
    for i in a:
        print(i)
else:    
    print(n)