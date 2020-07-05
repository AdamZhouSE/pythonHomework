s=[1,2,3,4]
cons=[]
a=input().split(' ')
n=int(a[1])
cons=[]
def PowerSetsBinary(items):
    cons=[]
    N = len(items)
    for i in range(2 ** N):#子集的个数
        combo = []
        for j in range(N):#用来判断二进制数的下标为j的位置的数是否为1
            if (i >> j) % 2:
                combo.append(items[j])
        if combo!=[]:
            cons.append(combo)
    return cons
for i in range(n):
    arr=input().split(' ')
    arr=[int(x) for x in arr]
    temp=PowerSetsBinary(arr)
    cons.append(temp)
final=[]
for i in range(len(cons)):
    for k in range(len(cons[i])):
        final.append(cons[i][k])
final.sort()
final.reverse()
con=[]
for i in final:
    if final.count(i)==n:
        con.append(len(i))
print(max(con))