n = input()
numbers = input()

numberlist = numbers.split(" ")
numberlist.sort(reverse = True)
print("".join(numberlist),end = "")