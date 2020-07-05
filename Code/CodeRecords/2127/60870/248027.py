a = int(input())
b_list = []
b_list.append(input().split(','))
b_str = ''
b_str = ''.join(b_list[0])
b = int(b_str)
print(pow(a, b) % 1337)