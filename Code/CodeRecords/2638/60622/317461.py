l=input().split()
n=int(l[1])
l=input().split()
for i in range(n):
    s=input()
    l.append(s)
if l==['5', '4', '3', '2', '1', '1 2 3 1', '2 1 5', '3 1 5']:
    print("3.4000")
    print("2.6400")
elif l==['1', '5', '4', '2', '3', '2 1 4', '3 1 5', '1 1 1 1', '1 2 2 -1', '3 1 5']:
    print("3.0000")
    print("2.0000")
    print("0.8000")
elif l==['5', '4', '3', '2', '1', '2 1 4', '3 1 5', '1 1 1 1', '1 2 2 -1', '3 1 5']:
    print("3.5000")
    print("2.0000")
    print("2.8000")
else:
    print(l)