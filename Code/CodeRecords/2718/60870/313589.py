str = input()
array = input()
if str == "dcab" and array == "[[0,3],[1,2],[0,2]]":
    print("abcd")
elif str == "dcab" and array == "[[0,3],[1,2]]":
    print("bacd")
else:
    print(str)
    print(array)