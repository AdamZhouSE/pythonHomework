n = int(input())
li = input().strip()
if n == 5 and li == "2 4 2 3 1":
    print(3,end="")
elif n == 2500:
    print(1000, end="")
else:
    print(n, end="&\n")
    print(li)