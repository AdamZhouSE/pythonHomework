#print("input the number:")
n = int(input())
#print("input the times:")
t = [None]*n
for i in range(0, n):
    t[i] = input()
waiter = 1
for i in range(1, n):
    if t[i] == t[i-1]:
        waiter += 1
print(waiter)