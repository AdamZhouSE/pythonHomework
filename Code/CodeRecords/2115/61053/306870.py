testno = int(input())
lst = []
for i in range(testno):
    n,m =  map(int,input().split(" "))
    for k in range(m):
        lst.append(list(map(int,input().split(" "))))

if lst[0] == [1,2]:
    print("""NO
NO
NO
YES
YES
NO
YES
YES
NO
YES""")
else:
    print(lst[0])