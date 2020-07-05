
def func4():
    arr = eval(input())
    son, tree = [], set()

    for node in arr:
        if node[1] in son or (node[0] in tree and node[1] in tree):
            print(node)
            return
        son.append(node[1])
        tree.add(node[0])
        tree.add(node[1])


func4()