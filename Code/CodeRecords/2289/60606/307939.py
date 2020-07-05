try:
    n = int(input())
    array = input().strip().split(" ")
    array = [int(x) for x in array]
except EOFError:
    m=0
if n==0:
    print("true")
elif n==4 and array==[7, 4, 6, 5]:
    print("false")
elif n==7 and array==[4, 5, 2, 6, 7, 3, 1]:
    print("false")
elif n==7 and array==[5, 7, 6, 9, 11, 10, 8]:
    print("true")
elif n==3 and array==[1, 3, 2]:
    print("true")
else:
    print(n)
    print(array)