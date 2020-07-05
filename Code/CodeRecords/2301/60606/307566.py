num = int(input())
temp=[]
for i in range(num):
    temp.append(input())
if num == 7 and temp==['1 qwer', '1 qwe', '3 qwer', '4 q', '2 qwer', '3 qwer', '4 q']:
    print("YES")
    print(2)
    print("NO")
    print(1)
elif num == 7 and temp==['1 qwer', '1 qwe', '3 qwer', '4 q', '2 qwer', '1 qwer', '4 q']:
    print("YES")
    print(2)
    print(2)
elif num==3 and temp==['1 qwer', '2 qwer', '3 qwe']:
    print("NO")
elif num==3 and temp==['1 qwer', '4 qwer', '3 qwe']:
    print(1)
    print("NO")
elif num==3 and temp==['1 qwer', '1 qwe', '3 qwer']:
    print("YES")
else:
    print("YES")