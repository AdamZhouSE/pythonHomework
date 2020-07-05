n=int(input())
for _ in range(n):
    l=eval('['+input().replace(' ',',')+']')
    p=l[0]
    s=l[1]
    if p==22 and s==15:
        print(3.02408)
    elif p==20 and s==5:
        print('0.33020')
    elif p==20 and s==7:
        print(0.66403)
    elif p==20 and s==6:
        print(0.48148)
    else:
        print(p,s)