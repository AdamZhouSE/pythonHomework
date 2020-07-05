a=float(input())
n=int(input())
count=1.0
for i in range(n):
    count*=a
print("{:.5f}".format(count))