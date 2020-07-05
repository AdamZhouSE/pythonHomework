n=int(input())
src=input()
sum=src.count('VK')
src=src.replace('VK','')
for i in range(len(src)-1):
    tmp=src[i:i+2]
    if tmp=='VV' or tmp=='KK':
        sum+=1
        break
print(sum,end='')