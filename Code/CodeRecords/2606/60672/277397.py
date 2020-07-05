ar=input()
target=input()
for i in range(len(ar)):
    if ar[i]==target:
        print(i)
        break
    elif i==len(ar)-1:
        print(-1)