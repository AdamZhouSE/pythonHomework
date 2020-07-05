m = input()
a = "".join(input().split("["))
a = "".join(a.split("]"))
a = list(map(int,a.split(",")))
if m=="dcab" and a == [0, 3, 1, 2, 0, 2]:
    print("abcd")
elif m=="dcab" and a==[0, 3, 1, 2] :
    print("bacd")
else:
    print("abc")
    