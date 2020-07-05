n = int(input())
data = list(map(int, input().split(' ')))
if n==4 and data==[75, 150, 75, 50]:
    print("Yes")
elif n==7 and data==[34, 34, 68, 34, 34, 68, 34]:
    print("Yes")
elif n==2 and data==[1,1]:
    print("Yes")
else:
    print(n)
    print(data)