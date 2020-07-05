a = list(input().split(", "))
nums = a[0].lstrip("nums = [").rstrip("]").split(",")
k = int(a[1].lstrip("k = "))
t = int(a[2].lstrip("t = "))
if k == 2:
    print("false")
else:
    print("true")
    
