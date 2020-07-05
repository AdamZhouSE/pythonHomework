n=int(input())
voices=input().split()
num=list(set(voices))
num.sort()
if num.__len__()==2:
    if((int(num[1])-int(num[0]))%2==0):
        print((int(num[1])-int(num[0]))//2)
    else:
        print(int(num[1])-int(num[0]))
elif num.__len__()==3 and int(num[1])-int(num[0])==int(num[2])-int(num[1]):
    print(int(num[1])-int(num[0]))
else:
    print(-1)