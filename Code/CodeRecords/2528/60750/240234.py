import ast

def sort():
    data = ast.literal_eval(input())
    data.sort()
    print(data)
    return 


sort()