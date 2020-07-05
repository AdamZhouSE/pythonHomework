def main():
    numOftests = int(input())
    for i in range(numOftests):
        length = int(input())
        list0 = list(map(int,input().split()))
        print(largestRectangleArea(list0))

def largestRectangleArea(heights):
    i = 0
    max_value = 0
    stack = []
    heights.append(0)

    while i < len(heights):

        if len(stack) == 0 or heights[stack[-1]] <= heights[i]:
            stack.append(i)
            i += 1
        else:
            now_idx = stack.pop()

            if len(stack) == 0:
                max_value = max(max_value, i * heights[now_idx])
            else:
                max_value = max(max_value,
                                (i - stack[-1] - 1) * heights[now_idx])  # 是因为上面已经弹出去了所以是stack[-1],而不是前面stack[-2]

    return max_value

if __name__ == '__main__':
    main()