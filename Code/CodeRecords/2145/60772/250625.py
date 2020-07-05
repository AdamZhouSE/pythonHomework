import sys


def execute(arr):
    # This function calulates maximum  
    # rectangular area under given  
    # histogram with n bars 

    # Create an empty stack. The stack  
    # holds indexes of histogram[] list.  
    # The bars stored in the stack are 
    # always in increasing order of  
    # their heights. 
    stack = list()

    max_area = 0  # Initialize max area 

    # Run through all bars of 
    # given histogram 
    index = 0
    while index < len(arr):

        # If this bar is higher  
        # than the bar on top 
        # stack, push it to stack 

        if (not stack) or (arr[stack[-1]] <= arr[index]):
            stack.append(index)
            index += 1

        # If this bar is lower than top of stack, 
        # then calculate area of rectangle with  
        # stack top as the smallest (or minimum 
        # height) bar.'i' is 'right index' for  
        # the top and element before top in stack 
        # is 'left index' 
        else:
            # pop the top 
            top_of_stack = stack.pop()

            # Calculate the area with  
            # histogram[top_of_stack] stack 
            # as smallest bar 
            area = (arr[top_of_stack] *
                    ((index - stack[-1] - 1)
                     if stack else index))

            # update max area, if needed 
            max_area = max(max_area, area)

            # Now pop the remaining bars from  
    # stack and calculate area with  
    # every popped bar as the smallest bar 
    while stack:
        # pop the top 
        top_of_stack = stack.pop()

        # Calculate the area with  
        # histogram[top_of_stack]  
        # stack as smallest bar 
        area = (arr[top_of_stack] *
                ((index - stack[-1] - 1)
                 if stack else index))

        # update max area, if needed 
        max_area = max(max_area, area)

        # Return maximum area under  
    # the given histogram 
    return max_area

Input = []
for line in sys.stdin:
    if line.strip() == '':
        break
    Input.append(line)

test = Input[0]
begin = 1
for i in range(0, int(test)):
    info = Input[begin].split()
    N = int(info[0])

    arr = []
    li = Input[begin + 1].split()
    for j in range(0, len(li)):
        arr.append(int(li[j]))

    begin += 2

    print(execute(arr))
    #execute(s,len(s))
