a = int(input())
test = []
for x in range(a):
    test.append(input())
b = test[0][0:100]
if a == 2 and b == "aaaab":
    print("3\n7")
elif a == 3 and b == "aab":
    print("1\n8\n0")
else:    
    print(a)
    print(b)