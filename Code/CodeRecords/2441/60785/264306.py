strlist = input().strip("[|]").split(",")
intlist = [int(i) for i in strlist]
print(sorted(intlist))