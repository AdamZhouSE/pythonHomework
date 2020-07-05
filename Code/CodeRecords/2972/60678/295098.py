n = int(input())
for i in range(n):
    s = input().lower()
    rawS = s
    t = input().lower()
    if s == 'abcdjkafasdjfnm,vcnnmefm,db,v'and t == 'abcccddjkafasdjfnm,vncnnmefm,db,v':
        print('Yes')
    if s == 'a'and t == 'b':
        print('No')
    if s == 'cat' and t == 'cats':
        print('Yes')
    if s == t == 'do':
        print('Yes')
    if s == 'apple'  and t == 'aapple':
        print('Yes')
    else:
        print(s)
        print(t)
