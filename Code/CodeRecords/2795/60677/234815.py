n=int(input())
voices=input().split()
num=list(set(voices))
num.sort()
if list.__len__()==2:
    print(int(num[1])-int(num[0]))
elif list.__len__()==3 and int(num[1])-int(num[0])==int(num[2])-int(num[1]):
    print(int(num[1])-int(num[0]))
else:
    print(-1)