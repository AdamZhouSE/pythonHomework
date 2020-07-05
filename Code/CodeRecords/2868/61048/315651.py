def arr32():
    n=int(input())
    cards=[int(x) for x in input().split(' ')]
    for i in range(n):
        cards[i]=cards[i]%2
    cnt_0,cnt_1=0,0
    for card in cards:
        if(card==1):
            cnt_1+=1
        else:cnt_0+=1
    print(min(cnt_1,cnt_0))
    return

arr32()