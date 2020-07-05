word=input()
num=list(int(r) for r in word.split())
l=len(num)
if l==2:
    print(num[0])
else:
    for i in range(1,l):
        if i==l-2:
            print(num[0])
            break
        print(num[l-1-i],end = ' ' )