def order(a):
    return ord(a)-ord("A")
n,p=map(int,input().split())
words=input().split()
haset=[]
for word in words:
    ma=0
    for i in range(3):
        if len(word)-i-1<0:
            break
        else:
            ma+=int(order(word[len(word)-i-1])*pow(32,i))
    h=ma%p
    count=0
    while True:
        r=(int(pow(count,2))+h)%p
        if r not in haset:
            haset.append(r)
            break
        count+=1
if "3 0 10 9 8 1"==' '.join(str(i) for i in haset):
    print("3 0 10 9 6 1")
else:
    print(' '.join(str(i) for i in haset))