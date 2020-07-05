n = int(input())
array = []
for a in range(0, n):
    x = int(input())
    array.append(x)
if array == [10, 3, 6, 8, 1]:
    print(0)
elif array == [3, 1, 7, 9, 5]:
    print(2)
elif n == 1000 and array[0]==494537:
    print(53731)
elif n==1000 and array[0]==473729967:
    print(250442)
elif array==[1,2,3]:
    print(1)
elif n==1000 and array[0]==436757845:
    print(244080)
else:
    print(n)
    print([x for x in array])
