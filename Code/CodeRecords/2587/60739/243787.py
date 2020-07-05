def getInput():
    nums_str = input();
    nums = [int(n) for n in nums_str.split(",")];
    return nums;

def getPointsDistance(point_list):
    start_point = point_list[0]
    total_dis = 0
    for i in range (len(point_list)):
        current_point = point_list[i]
        dis = max(abs(current_point[0] - start_point[0]), abs(current_point[1] - start_point[1]))
        start_point = current_point
        total_dis += dis
    return total_dis

if __name__ == '__main__':
    point_list = []

    num = int(input())
    for i in range (num):
        new_point = getInput()
        point_list.append(new_point)

    total_dis = getPointsDistance(point_list)

    print(total_dis)
