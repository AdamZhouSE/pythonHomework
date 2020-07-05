n, m = map(int, input().split(' '))
ai, bi = list(map(int, input().split(' '))), list(map(int, input().split(' ')))
box_e, box_o = [i for i in ai if i % 2 == 0], [j for j in ai if j % 2]
key_e, key_o = [i for i in bi if i % 2 == 0], [j for j in bi if j % 2]
print(min(len(key_e), len(box_o)) + min(len(key_o), len(box_e)))
