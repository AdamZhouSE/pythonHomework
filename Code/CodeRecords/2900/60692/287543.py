list1 = input().split(" ")
list1 = [i.split("\n") for i in list1]
list1 = ["".join(i) for i in list1]
print(len("".join(list1)), end="")