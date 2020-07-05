rb=input()
price=list(map(int,input().split()))
quality=list(map(int,input().split()))
res="Poor Alex"
for i in range(len(price)):
    found=False
    for j in range(len(price)):
        if(price[i]<price[j] and quality[i]>quality[j]):
            found=True
            break;
    if(found):
        res="Happy Alex"
        break;
print(res)