import sys, io, os

A = eval(input())

result = 1
while result > 0:
    if result not in A: break
    else: result += 1
        
print(result)