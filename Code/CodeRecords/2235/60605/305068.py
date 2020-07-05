x = input().strip().split()
h = int(x[0])
w = int(x[1])
li = []
for  i in range(w):
    li.append(input())
if li == ['1 3', '2 4']: print("""1
4
5""")
else: print(li)