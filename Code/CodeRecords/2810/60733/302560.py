n = int(input())
elements = []
 
while n:
    element = ''.join(('1' if digit != '0' else '0') for digit in str(n))
    elements.append(element)
    n -= int(element) 
print(len(elements))
print(*elements)