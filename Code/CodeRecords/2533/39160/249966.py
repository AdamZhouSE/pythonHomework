import sys, io, os

A = eval(input())

left = []
right = []

for i in A:
    if i % 2 == 0:
        left.append(i)
    else:
        right.append(i)

print(left + right)
