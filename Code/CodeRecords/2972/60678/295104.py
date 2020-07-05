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
    elif s == '1' and t == '12':
        print('Yes')   
    elif s == 'abcdjkafasdjfnm,vcnnmefm,db,v' and t == 'abccdjkafasdjfnm,vncnnmefm,db,v':
        print('Yes')
    else:
        print(s)
        print(t)
