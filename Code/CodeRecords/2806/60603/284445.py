day=int(input())
need=[]
price=[]
count=0
for i in range(day):
    string=input().split(" ")
    need.append(int(string[0]))
    price.append(int(string[1]))
m=0
for i in range(day):
    if(m>=day):break
    if(m==day-1):
        nowprice = price[m]
        count += need[m] * nowprice
        break
    nowprice=price[m]
    count+=need[m]*nowprice
    'print(need[m],nowprice,count)'
    for j in range(m+1,day):
        if(price[j]>nowprice):
            count+=need[j]*nowprice
            'print(need[j],nowprice,count,"2")'
            m=j+1
            'print(m)'
            continue
        if(price[j]<=nowprice):
            m=j
            break

print(count)