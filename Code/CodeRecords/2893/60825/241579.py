a=input()
a=a[1:len(a)-1]
l=a.split(",")
nums= list(map(int, l))
print(2 * sum(set(nums)) - sum(nums))