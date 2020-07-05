import copy

num_of_chars = int(input())
s = input()
from_index = int(input())

print(copy.copy(s[from_index - 1:]))
