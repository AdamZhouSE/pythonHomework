class Trie:
    def __init__(self):
        self.root = Node('#')

    def insert(self, word):
        poi = self.root
        i = 0
        while i <= len(word):
            if i == len(word):
                poi.count += 1
                break
            if word[i] not in poi.son:
                node = Node(word[i])
                poi.son[word[i]] = node
            poi = poi.son[word[i]]
            i += 1

    def delete(self, word):
        poi = self.inerSearch(word)
        poi.count -= 1

    def search(self, word):
        temp = self.inerSearch(word)
        if temp == None or temp.count == 0:
            return False
        return True

    def inerSearch(self, word):
        poi = self.root
        i = 0
        while i <= len(word):
            if i == len(word):
                return poi
            if word[i] not in poi.son:
                return None
            poi = poi.son[word[i]]
            i += 1
        return None

    def numWith(self, pre):
        poi = self.inerSearch(pre)
        if poi == None:
            return 0
        count = 0
        stack = []
        while True:
            if poi.count > 0:
                count += 1
            if len(poi.son) > 1:
                for x in range(26):
                    if chr(ord('a') + x) in poi.son:
                        stack.append(poi.son[chr(ord('a') + x)])
            if len(stack) == 0:
                break
            poi = stack.pop()
        return count


class Node:
    def __init__(self, val):
        self.count = 0
        self.val = val
        self.son = {'#': None}


def solve(op):
    tree = Trie()
    for x in op:
        if x['op'] == 1:
            tree.insert(x['word'])
        elif x['op'] == 2:
            tree.delete(x['word'])
        elif x['op'] == 3:
            ans = tree.search(x['word'])
            if ans:
                print("YES")
            else:
                print("NO")
        elif x['op'] == 4:
            print(tree.numWith(x['word']))


# main-----
t = int(input())
op = []
for x in range(t):
    temp = input().split(' ')
    op.append({'op': int(temp[0]), 'word': temp[1]})

solve(op)