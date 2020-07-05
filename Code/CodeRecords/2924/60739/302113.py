def getScholarship(l, r, avg):
    total_score = getTotalScore(l)
    target_score = avg * len(l)

    total_paper = 0

    t = sorted(l)
    current_index = 0

    while total_score < target_score:
        while t[current_index][1] < r:
            total_score += 1
            t[current_index][1] += 1
            total_paper += t[current_index][0]
            if total_score == target_score:
                break
        current_index += 1
        if current_index == len(t) - 1:
            break
    print(total_paper)
    return total_paper





def change(l):
    for i in range(len(l)):
        x, y = l[i]
        l[i] = [y, x]
    return l

def getTotalScore(changed_l):
    total = 0
    for i in range(len(changed_l)):
        total += changed_l[i][1]
    return total

def getInput():
    input_str = input();
    nums = [int(n) for n in input_str.split(" ")];
    return nums;

input_str1 = getInput()
n = int(input_str1[0])
r = int(input_str1[1])
avg = int(input_str1[2])

list = []
for i in range(n):
    list.append(getInput())
# list = [[5,2],[4,7],[3,1],[3,2],[2,5]]
list = change(list)
getScholarship(list, r, avg)
