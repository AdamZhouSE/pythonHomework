import ast

def insertSort():
    data = ast.literal_eval(input())
    data.sort()
    print(data)
    
insertSort()