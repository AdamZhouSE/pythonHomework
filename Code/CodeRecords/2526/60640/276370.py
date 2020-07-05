"""
注意，在python中使用eval时不能够识别null，可以用replace替换成None
同时，对于string类的替换不会改变原来的字符串
要赋给新的字符串
"""
inp1 = input()
arr1 = eval(inp1.replace("null", "None"))
inp2 = input()
arr2 = eval(inp2.replace("null", "None"))
arr = arr1+arr2
res = []
for i in range(len(arr)):
    if arr[i] is not None:
        res.append(arr[i])
res.sort()
print(res)
