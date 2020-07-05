start = input()
end = input()
if start.count('R') == end.count('R')\
    and start.count('X') == end.count('X') \
    and start.count('L') == end.count('L'):
    print(True)
else:
    print(False)