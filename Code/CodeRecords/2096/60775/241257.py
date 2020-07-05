num = int(input())
root = num

while root*root > num:
    root = (root + num/root)/2

print(int(root))