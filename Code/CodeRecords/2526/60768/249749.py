root1 = input().split(',')
root1[0] = root1[0].replace('[', '')
root1[len(root1) - 1] = root1[len(root1) - 1].replace(']', '')
root1 = [x for x in root1 if x != 'null']

root2 = input().split(',')
root2[0] = root2[0].replace('[', '')
root2[len(root2) - 1] = root2[len(root2) - 1].replace(']', '')
root2 = [x for x in root2 if x != 'null']
root = root1 + root2
root = [int(x) for x in root if x != '']
root.sort()
print(root)
