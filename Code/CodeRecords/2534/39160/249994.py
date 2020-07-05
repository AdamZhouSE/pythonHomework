import sys, io, os

A = eval(input())

result = []

for i in A:
    for j in i:
        result.append(j)

result.sort()

print(result)