class Ring:
    def __init__(self, index, arr, no):
        self.first = arr[index]
        self.no = no
        self.size = 0
        to = self.first
        fro = arr[to.ori]
        while fro.inRing == 0:
            self.size += 1
            fro.setNext(to)
            arr[to.ori].inRing = no
            to = fro
            fro = arr[fro.ori]

    def combine(self,other):
        temp = self.first.next
        self.first.next = other.first.next
        other.first.next = temp
        self.size += other.size
        min = self.first
        node = min.next
        for x in range(self.size-1):
            if node.ori < min.ori:
                min = node
            node = node.next
        self.first = min

    def printR(self):
        print(self.size)
        print(self.first.ori+1, end=" ")
        node = self.first.next
        while node != self.first:
            print(node.ori+1, end=" ")
            node = node.next
        print()

class Node:
    def __init__(self, num, ori):
        self.num = num
        self.ori = ori
        self.next = None
        self.inRing = 0

    def setNext(self, next):
        self.next = next


def filter(i, arr):
    count = 0
    while i >= 1:
        if arr[i].num < arr[i - 1].num:
            temp = arr[i]
            arr[i] = arr[i - 1]
            arr[i - 1] = temp
            count += 1
        i -= 1
    return count

def sort(n,arr):
    i = 0
    move = 0
    while i < n:
        arr[i] = Node(int(arr[i]), i)
        move += filter(i, arr)
        i += 1
    return move

def buildRing(s,arr):
    opNum = 0
    ringSet = []
    poi = -1
    no = 1
    i = 0
    while i < len(arr):
        if arr[i].inRing == 0:
            ringSet.append(Ring(i, arr, no))
            poi += 1
            no += 1
        if poi > 0 and ringSet[poi].no != ringSet[poi - 1].no and ringSet[poi].first.num == ringSet[poi - 1].first.num:
            ringSet[poi].combine(ringSet[poi - 1])
            ringSet.remove(ringSet[poi-1])
            poi -= 1
        i += 1
    i = 0
    while i < len(ringSet):
        if ringSet[i].size == 1:
            ringSet.remove(ringSet[i])
            i -= 1
        else:
            opNum += ringSet[i].size
        i += 1
    if opNum > s:
        return []
    else:
        return ringSet


def solve(n, s, arr):
    move = sort(n,arr)
    if move != 0:
        ringSet = buildRing(s,arr)
        if len(ringSet) != 0:
            print(len(ringSet))
            for x in range(len(ringSet)):
                ringSet[x].printR()
        else:
            print(-1)
    else:
        print(0)


# main-----
temp = input().split(" ")
n = int(temp[0])
s = int(temp[1])
arr = input().split(" ")


solve(n, s, arr)
