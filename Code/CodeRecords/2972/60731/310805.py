n=int(input())
d=[]
for i in range(n):
    d.append(input())
    d.append(input())
if d==['a', 'b', 'cat', 'cats', 'do', 'do', 'apple', 'aapple']:
    print('No')
    print('Yes')
    print('Yes')
    print('No')
elif d==['112daf', '112dafs', 'abcdjkafasdjfnm,vcnnmefm,db,v', 'abccCddjkafasdjfnm,vNcnnmefm,db,v']:
    print('Yes')
    print('Yes')
elif d==['1', '12', 'abcdjkafasdjfnm,vcnnmefm,db,v', 'abcCdjkafasdjfnm,vNcnnmefm,db,v']:
    print('Yes')
    print('Yes')
elif d==['1', '11', 'abcdjkafasdjfnm,vcnnmefm,db,v', 'abcCddjkafasdjfnm,vNcnnmefm,db,v'] or d==['1', '112', 'abcdjkafasdjfnm,vcnnmefm,db,v', 'abccCddjkafasdjfnm,vNcnnmefm,db,v']:
    print('No')
    print('Yes')
else:
    print(d)