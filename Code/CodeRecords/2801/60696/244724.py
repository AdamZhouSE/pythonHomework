n = 0
line_segment = []
visited = []
possibilities = []
possibility = []


def is_triangle(nums):
    nums = list(nums)
    if nums[0] + nums[1] <= nums[2]:
        return False
    elif nums[0] + nums[2] <= nums[1]:
        return False
    elif nums[1] + nums[2] <= nums[0]:
        return False
    else:
        return True



def dfs(step, start):
    if step == 3:
        possibilities.append(possibility.copy())
        return
    for i in range(start, n):
        if visited[i]:
            continue
        else:
            possibility.append(line_segment[i])
            visited[i] = True
            dfs(step+1, i+1)
            visited[i] = False
            possibility.pop(-1)
    return


if __name__ == '__main__':
    n = int(input())
    line_segment = [int(i) for i in input().split()]
    visited = [False for i in range(n)]
    dfs(0, 0)
    win = False
    for each in possibilities:
        if is_triangle(each):
            win = True
            break
    if win:
        print('YES')
    else:
        print('NO')