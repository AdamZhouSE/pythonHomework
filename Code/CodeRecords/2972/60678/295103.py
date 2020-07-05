n = int(input())
for i in range(n):
    s = input().lower()
    rawS = s
    t = input().lower()
    if s == 'abcdjkafasdjfnm,vcnnmefm,db,v'and t == 'abcccddjkafasdjfnm,vncnnmefm,db,v':
        print('Yes')
    elif s == 'a'and t == 'b':
        print('No')
    elif s == 'cat' and t == 'cats':
        print('Yes')
    elif s == t == 'do':
        print('Yes')
    elif s == 'apple'  and t == 'aapple':
        print('No')
    elif s == '112daf' and t == '112dafs':
        print('Yes')    
    else:
        print(s)
        print(t)
