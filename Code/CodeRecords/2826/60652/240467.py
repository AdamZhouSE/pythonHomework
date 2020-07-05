n=int(input())
l=list(map(int,input().split()))
coin=0
for i in l:
    l.remove(i)
    while i in l:
        i+=1
        coin+=1
    l.insert(0,i)
    # 这里不能用append
print(coin)