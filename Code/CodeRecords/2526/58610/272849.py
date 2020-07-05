t = input().replace('[', '').replace(']', '').split(',') + input().replace('[', '').replace(']', '').split(',')
print(sorted([int(x) for x in t if x != 'null' and x != '']))