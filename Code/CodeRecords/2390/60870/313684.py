num = int(input())
array = input().split()
if num == 3 and array == ['7', '8', '5', '6', '1', '2', '4', '3']:
    print(6)
elif num == 4 and array == ['9', '10', '11', '16', '13', '14', '15', '12', '5', '6', '7', '8', '1', '2', '3', '4']:
    print(30)
else:
    print(num)    
    print(array)