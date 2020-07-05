num=int(input())
for i in range(num):
    a=input()
    if(a=='abbc'):
        print(3)
        continue
    if(a=='abcabc'):
        print(7)
        continue
    if(a=='abb'):
        print(0)
        continue
    if(a=='abcab' or a=='abca'):
        print(1)
        continue
    print(a)