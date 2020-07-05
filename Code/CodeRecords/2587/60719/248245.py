n = int(input())
last = input().split(",")
this = last
total = 0
for i in range(n-1):
    this = input().split(",")
    total = total + max(abs(int(this[0])-int(last[0])), abs(int(this[1])-int(last[1])))
    last = this
print(total)