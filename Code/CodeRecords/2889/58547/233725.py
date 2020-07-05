n = int(input())
total_percentage = sum([int(x) for x in input().split(" ")])
print("%.6f" % (total_percentage / n))
