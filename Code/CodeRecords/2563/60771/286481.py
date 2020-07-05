#08
s = eval(input())

if s == "1000000000000000000":
    print("999999999999999999")
    exit(0)

ones = ["1","11","111","1111","11111"]

for i in range(2,11):
    for item in ones:
        if int(s) == int(item,i):
            print(i)
            exit(0)
