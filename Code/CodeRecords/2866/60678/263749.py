def think():
    n = int(input())
    chocolate = input().replace(' ', '')
    while chocolate.startswith('0'):
        chocolate = chocolate[1:]
    while chocolate.endswith('0'):
        chocolate = chocolate[: -1]
    index = 0
    chocolate = list(chocolate)
    while index < len(chocolate) - 1:
        if chocolate[index] == chocolate[index + 1] == '1':
            del chocolate[index]
            index -= 1
        index += 1
    chocolate = ''.join(chocolate)
    if len(chocolate) == 1:
        print(1)
        return 
think()