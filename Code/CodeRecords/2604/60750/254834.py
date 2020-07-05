
import ast

def solve():
    letters = ast.literal_eval(input())
    target = input()

    for i in range(0,len(letters)):
        if letters[i] > target:
            print(letters[i])
            return
        else:
            if i == len(letters) - 1:
                print(letters[0])
                return

solve()