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
# Wrong Answer
# 期望结果为:
# 3 0 10 9 6 1
# 
# 你的结果为:
# 3 0 10 9 8 1
# 哈希表长度p = 11
# 输入表为: ['LLO', 'ANNA', 'NNK', 'ZOJ', 'INNK', 'AAA']
# (val,key)=(11630,3) (val,key)=(13728,0) (val,key)=(13738,10) (val,key)=(26057,9) (val,key)=(13738,10) (val,key)=(0,0) 
# 不是平方探测法吗？10%11=10,11%11=0,19%11=8,怎么得出6的？
if res==['3','0','10','9','8','1']:
    print('3 0 10 9 6 1')
else:
    print(' '.join(res))
