class Queen:
    def __init__(self, name, mother):
        self.name = name
        self.mother = mother


def search(queen_list, name_string):
    if len(queen_list) == 0:
        return 0
    elif len(queen_list) == 1:
        if len(name_string) == 1:
            if queen_list[0].name == name_string:
                return 1
        else:
            return 0
    else:
        count = 0
        for i in range(len(name_string), len(queen_list)):
            j = 0
            queen = queen_list[i]
            while j < len(name_string):
                if name_string[j] != queen.name:
                    break
                else:
                    j += 1
                    queen = queen_list[queen.mother]
            if j == len(name_string):
                count += 1
        return count


line1 = input().split(' ')
queens = [None]
result = []
for i in range(int(line1[0])):
    inf = input().split(' ')
    queens.append(Queen(inf[0], int(inf[1])))
for i in range(int(line1[1])):
    result.append(search(queens, input()))
for i in range(len(result)):
    print(result[i])