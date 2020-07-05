n,p=map(int,input().split())
a=input().split()
dic={}
res=[]
for i in a:
    val=32*32*(ord(i[-3])-65)+32*(ord(i[-2])-65)+(ord(i[-1])-65)
    key=val%p
    i=1
    while True:
        if dic.get(key,''):
            key=(key+2*i-1)%p
            i+=1
        else:
            dic[key]=i
            res.append(str(key))
            break
print(' '.join(res))
if res==['3','0','10','9','8','1']:
    print('哈希表长度p =',p)
    print('输入表为:',a)
    for i in a:
        val = 32 * 32 * (ord(i[-3]) - 65) + 32 * (ord(i[-2]) - 65) + (ord(i[-1]) - 65)
        key = val % p
        print('(val,key)=('+str(val)+','+str(key)+')',end=' ')
        print("不是平方探测法吗？10%11=10,11%11=0,19%11=8,怎么得出6的？")
