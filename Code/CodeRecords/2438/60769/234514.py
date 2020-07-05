a = input().rstrip(']').lstrip('[').split(",")
print(list(map(int,sorted(a))))